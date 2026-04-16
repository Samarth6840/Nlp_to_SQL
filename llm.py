# llm.py
from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)

def ask_llm(user_question, schema_info, mode="sql"):
    if mode == "sql":
        prompt = f"""
You are a SQL expert.
Database engine: SQLite
Table name: data

Schema:
{schema_info}

Convert the user's question into ONE valid SQLite SELECT query only.
Rules:
- Return only SQL
- Do not use information_schema
- Do not use DELETE, DROP, TRUNCATE, ALTER, UPDATE, or INSERT
- Use only the table name data
- If the user asks for column names, use PRAGMA table_info(data)
- If the question is not answerable with SQL, return: NOT_SQL
Question: {user_question}
"""
    else:
        prompt = f"""
You are a helpful SQL tutor and coding assistant.
Explain the following in simple language and give code examples when useful:
{user_question}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )
    return response.text.strip()