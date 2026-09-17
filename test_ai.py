from ai.gemini_service import generate_sql

question = input("Ask a question: ")

sql = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql)