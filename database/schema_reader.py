import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "school.db"


def get_schema():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%';
    """)

    tables = cursor.fetchall()

    schema = ""

    for table in tables:
        table_name = table[0]
        schema += f"\nTable: {table_name}\n"

        cursor.execute(f"PRAGMA table_info({table_name})")

        columns = cursor.fetchall()

        for col in columns:
            schema += f"    {col[1]} ({col[2]})\n"

    conn.close()

    return schema


if __name__ == "__main__":
    print(get_schema())