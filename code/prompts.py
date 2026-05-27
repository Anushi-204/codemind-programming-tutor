# prompts.py

EXPLAIN_PROMPT = """
Explain the programming concept "{concept}" for a {level} learner.

Include:
- Simple explanation
- Syntax
- Example
"""

PRACTICE_PROMPT = """
Generate {level} practice questions for the concept "{concept}".
Do NOT provide solutions.
"""

CHAT_PROMPT = """
Answer the following programming question clearly with examples:
{question}
"""

ROADMAP_PROMPT = """
Create a structured learning roadmap for "{topic}".
Cover beginner to advanced levels.
"""

TASK_PROMPT = """
Generate a {level}-level Python mini project based on the concept "{concept}".

Include:
1. Project Title
2. Problem Statement
3. Functional Requirements
4. Constraints
5. Hints (DO NOT provide solution code)

The task should encourage hands-on learning.
"""
