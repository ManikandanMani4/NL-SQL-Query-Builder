import streamlit as st


from ai.groq_service import generate_sql
from database.query_executor import execute_query
from security.safety_check import is_safe

st.set_page_config(
    page_title="NL to SQL Query Builder",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Natural Language to SQL Query Builder")

st.write("Ask your database question in normal English.")

question = st.text_input(
    "Enter your question",
    placeholder="Example: Show top 3 school students by marks"
)

if st.button("Generate SQL"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    try:
        # Generate SQL using Groq
        sql = generate_sql(question)

        st.subheader("Generated SQL")
        st.code(sql, language="sql")

        # Safety Check
        if not is_safe(sql):
            st.error("Unsafe query detected. Only SELECT queries are allowed.")
            st.stop()

        # Execute Query
        result = execute_query(sql)

        if not result["success"]:
            st.error(result["error"])
            st.stop()

        columns = result["columns"]
        rows = result["rows"]

        st.subheader("Query Result")

        if rows:
           table_data = [dict(zip(columns, row)) for row in rows]
           st.table(table_data)
        else:
            st.info("No records found.")

    except Exception as e:
        st.error(f"Error: {e}")