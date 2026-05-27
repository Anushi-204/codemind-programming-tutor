# tutor.py

import os
from dotenv import load_dotenv
from groq import Groq
from prompts import (
    EXPLAIN_PROMPT,
    PRACTICE_PROMPT,
    CHAT_PROMPT,
    ROADMAP_PROMPT,
    TASK_PROMPT
)

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.1-8b-instant"

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def explain_concept(concept, level):
    return call_llm(EXPLAIN_PROMPT.format(concept=concept, level=level))


def generate_practice(concept, level):
    return call_llm(PRACTICE_PROMPT.format(concept=concept, level=level))


def chat_with_tutor(question):
    return call_llm(CHAT_PROMPT.format(question=question))


def generate_roadmap(topic):
    return call_llm(ROADMAP_PROMPT.format(topic=topic))


# ✅ NEW FEATURE
def generate_task(concept, level):
    return call_llm(TASK_PROMPT.format(concept=concept, level=level))
