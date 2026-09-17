from groq import Groq
from config import GROQ_API_KEY
from ai.prompt_builder import build_prompt

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

schema = """
Employees(
    employee_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    age INTEGER,
    department TEXT,
    designation TEXT,
    salary REAL,
    attendance REAL,
    experience INTEGER,
    email TEXT,
    phone TEXT,
    city TEXT,
    state TEXT,
    country TEXT,
    joining_date DATE,
    manager_id INTEGER,
    status TEXT
)
"""

def generate_sql(question):
    prompt = build_prompt(schema, question)

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

    # Remove markdown if the model returns it
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql