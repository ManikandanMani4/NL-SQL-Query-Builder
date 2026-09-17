# NL-SQL-Query-Builder

## About the Project

NL-SQL-Query-Builder is a smart database query application that allows users to interact with databases using natural-language questions instead of manually writing SQL queries.

The system accepts questions in simple English, understands the user's request, and converts it into an appropriate SQL query. The generated query is then executed against the connected database, and the results are displayed in a clear and user-friendly format.

## Key Features

- Convert natural-language questions into SQL queries
- Execute generated SQL queries
- Display database results in a structured format
- Understand database tables and columns
- Validate generated queries
- Handle SQL errors with meaningful messages
- Maintain query history
- Support easy interaction with structured database information

## Example

**User Question:**

> Show all students from the IT department.

**Generated SQL:**

```sql
SELECT * FROM students
WHERE department = 'IT';
