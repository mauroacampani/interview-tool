RULES_PROMPT = '''Analyze the following interview conversation and generate:

- Overall score (1-10)
- Communication evaluation
- Strengths
- Weaknesses
- Final recommendation

Return the response in Spanish.
'''
RESPONSE_PROMPTS = '''This is the interview you should be evaluating. You are merely a tool and should not engage in conversation.'''
def build_feedback_prompt(conversation_history):
    return  [{"role": "system", "content": RULES_PROMPT},
            {"role": "user", "content": f"{RESPONSE_PROMPTS}: {conversation_history}"}]
