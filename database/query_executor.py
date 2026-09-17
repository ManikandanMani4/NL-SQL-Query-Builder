import sqlite3
from pathlib import Path

# Database Path
DB_PATH = Path(__file__).parent / "school.db"


def execute_query(sql_query):
    """
    Execute the SQL query and return the results.
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(sql_query)

        # SELECT queries
        if sql_query.strip().upper().startswith("SELECT"):
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            conn.close()

            return {
                "success": True,
                "columns": columns,
                "rows": rows
            }

        # INSERT / UPDATE / DELETE
        conn.commit()
        affected = cursor.rowcount

        conn.close()

        return {
            "success": True,
            "message": f"Query executed successfully. {affected} row(s) affected."
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


if __name__ == "__main__":

    query = "SELECT * FROM SchoolStudents;"

    result = execute_query(query)

    if result["success"]:

        if "rows" in result:
            print(result["columns"])

            for row in result["rows"]:
                print(row)

        else:
            print(result["message"])

    else:
        print(result["error"])