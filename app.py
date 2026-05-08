from openai import OpenAI
import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from prompts.interview_prompts import build_interview_prompt
from prompts.feedback_prompts import build_feedback_prompt

st.set_page_config(page_title="Chat Streamlit", page_icon="speech_balloon")
st.title("ChatBot")

if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False

#Recuento de mensajes de usuario
if "user_message_count" not in st.session_state:
    st.session_state.user_message_count = 0


#Si se le ha mostrado el feedback al usuario
if "feedback_shown" not in st.session_state:
    st.session_state.feedback_shown = False

if "messages" not in st.session_state:
    st.session_state.messages = []

#Finalizacion de la entrevista
if "chat_complete" not in st.session_state:
    st.session_state.chat_complete = False

def complete_setup():
    st.session_state.setup_complete = True

def show_feedback():
    st.session_state.feedback_shown = True

if not st.session_state.setup_complete:

    st.subheader("Información Personal", divider="rainbow")

    if "name" not in st.session_state:
        st.session_state["name"] = ""
    if "experience" not in st.session_state:
        st.session_state["experience"] = ""
    if "skills" not in st.session_state:
        st.session_state["skills"] = ""

    st.session_state["name"] = st.text_input(label="Nombre", value=st.session_state["name"], max_chars=40, placeholder="Ingrese su nombre")

    st.session_state["experience"] = st.text_area(label="Experience", value=st.session_state["experience"], height=None, max_chars=200, placeholder="Describa su experiencia")

    st.session_state["skills"] = st.text_area(label="Skills", value=st.session_state["skills"], height=None, max_chars=200, placeholder="Liste sus skills")

    st.subheader("Compañia y Posición", divider="rainbow")

    if "level" not in st.session_state:
        st.session_state["level"] = "Junior"
    if "position" not in st.session_state:
        st.session_state["position"] = "Data Scientist"
    if "company" not in st.session_state:
        st.session_state["company"] = "Amazon"

    col1, col2 = st.columns(2)
    with col1:
        st.session_state["level"] = st.radio(
            "Seleccione el nivel",
            key="visibility",
            options=["Junio", "Mid-level", "Senior"],
        )

    with col2:
        st.session_state["position"] = st.selectbox(
            "Seleccione una posición",
            ("Data Scientist", "Data engineer", "Bi Analyst", "Financial Analyst")
        )

    st.session_state["company"] = st.selectbox(
            "Seleccione una compañía",
            ("Amazon", "Meta", "Udemy", "365 Company", "Nestle", "LinkedIn", "Spotify")
        )


    if st.button("Comience la Entrevista", on_click=complete_setup):
        st.write("Configuracion completa. Comenzando la entrevista....")

if st.session_state.setup_complete and not st.session_state.feedback_shown and not st.session_state.chat_complete:

    st.info(
        """
        Comience por presentarse.
        """,
        icon="👋🏻"
    )
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o-mini"


    if not st.session_state.messages:
        st.session_state.messages = [{
            "role": "system", 
            "content": build_interview_prompt(name=st.session_state.name, experience=st.session_state.experience, company=st.session_state.company, position=st.session_state.position, level=st.session_state.level, skills=st.session_state.skills)
            }]

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    if st.session_state.user_message_count < 5:
        if prompt := st.chat_input("Tu Pregunta.", max_chars=1000):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            if st.session_state.user_message_count < 4:
                with st.chat_message("assistant"):
                    stream = client.chat.completions.create(
                        model = st.session_state["openai_model"],
                        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                        stream=True,
                        temperature=1
                    )
                    response = st.write_stream(stream)
                
                st.session_state.messages.append({"role": "assistant", "content": response})
            
            st.session_state.user_message_count += 1

    if st.session_state.user_message_count >= 5:
        st.session_state.chat_complete = True

if st.session_state.chat_complete and not st.session_state.feedback_shown:
    if st.button("Obtener Feedback", on_click=show_feedback):
        st.write("Buscando Feedback")


if st.session_state.feedback_shown:
    st.subheader("Feedback")

    conversation_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])

    feedback_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    feedback_completion = feedback_client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=build_feedback_prompt(conversation_history),
        temperature=1
    )

    st.write(feedback_completion.choices[0].message.content)

    if st.button("Reiniciar Entrtevista", type="primary"):
        streamlit_js_eval(js_expressions="parent.window.location.reload()")