def build_prompt(schema, question):
    return f"""
You are an SQLite expert.

Database Schema:
{schema}

Rules:
1. Generate only SQLite SQL.
2. Return ONLY the SQL query.
3. Do  not explain Anything .
4. Do not use markdown.
5. Use only the tables and columns provided.

User Question:
{question}
"""