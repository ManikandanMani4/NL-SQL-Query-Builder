import sqlite3
from pathlib import Path

# Path to the SQLite database
DB_PATH = Path(__file__).parent / "education.db"


def get_connection():
    """
    Returns a connection to the SQLite database.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def test_connection():
    """
    Test whether the database connection is working.
    """
    try:
        conn = get_connection()
        conn.close()
        print("✅ Database connected successfully!")
    except Exception as e:
        print(f"❌ Connection failed: {e}")


if __name__ == "__main__":
    test_connection()