from groq import Groq
import os
from dotenv import load_dotenv

from database.schema_reader import get_schema

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)


def generate_sql(user_question):
    """
    Generate SQL query from natural language.
    """

    schema = get_schema()

    prompt = f"""
You are an expert SQLite SQL developer.

Database Schema:

{schema}

Table Usage Rules:
- Use SchoolStudents for school student-related questions.
- Use CollegeStudents for college student-related questions.
- Use Employees for employee-related questions.

Examples:
Question: Show top 3 school students by marks
SQL:
SELECT * FROM SchoolStudents ORDER BY marks DESC LIMIT 3;

Question: Show top 5 college students by cgpa
SQL:
SELECT * FROM CollegeStudents ORDER BY cgpa DESC LIMIT 5;

Question: Show top 3 employees by salary
SQL:
SELECT * FROM Employees ORDER BY salary DESC LIMIT 3;

Important Rules:
1. Return ONLY SQL.
2. Do NOT explain anything.
3. Do NOT use markdown.
4. Do NOT use ```sql```.
5. Use ONLY the tables and columns from the schema.
6. Never invent table names.
7. Never invent column names.
8. Use SQLite syntax only.
9. If the question cannot be answered using the schema, return exactly:
INVALID_QUERY

User Question:
{user_question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    sql = response.choices[0].message.content.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql


if __name__ == "__main__":

    question = "Show top 5 school students by marks"

    sql = generate_sql(question)

    print(sql)