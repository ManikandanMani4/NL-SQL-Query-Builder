import sqlite3

from pathlib import Path

DB_PATH = Path(__file__).parent / "school.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ==========================
# School Students Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS SchoolStudents(
    student_id INTEGER PRIMARY KEY,
    roll_number INTEGER UNIQUE,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    age INTEGER,
    class TEXT,
    section TEXT,
    attendance REAL,
    marks REAL,
    grade TEXT,
    city TEXT,
    phone TEXT
)
""")

# ==========================
# College Students Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS CollegeStudents(
    student_id INTEGER PRIMARY KEY,
    register_number TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    age INTEGER,
    department TEXT,
    year INTEGER,
    semester INTEGER,
    cgpa REAL,
    attendance REAL,
    placement_status TEXT,
    city TEXT,
    phone TEXT
)
""")

# ==========================
# Employees Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees(
    employee_id INTEGER PRIMARY KEY,
    employee_code TEXT UNIQUE,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    age INTEGER,
    department TEXT,
    designation TEXT,
    salary REAL,
    attendance REAL,
    city TEXT,
    phone TEXT
)
""")

# ==========================
# Insert School Students
# ==========================
school_students = [
    (1,101,"Rahul","Sharma","Male",16,"10","A",95,480,"A+","Chennai","9876543210"),
    (2,102,"Priya","Kumar","Female",15,"10","B",90,460,"A","Madurai","9876543211"),
    (3,103,"Arjun","Raj","Male",16,"11","A",85,430,"B+","Salem","9876543212"),
    (4,104,"Anitha","Devi","Female",17,"12","A",98,495,"A+","Coimbatore","9876543213"),
    (5,105,"Kavin","Murugan","Male",15,"9","C",80,400,"B","Karur","9876543214")
]

cursor.executemany("""
INSERT OR REPLACE INTO SchoolStudents
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
""", school_students)

# ==========================
# Insert College Students
# ==========================
college_students = [
    (1,"CSE001","Vijay","Kumar","Male",20,"CSE",3,5,8.9,94,"Placed","Chennai","9876500001"),
    (2,"IT002","Divya","Rani","Female",19,"IT",2,3,8.5,91,"Not Placed","Madurai","9876500002"),
    (3,"ECE003","Sanjay","Raj","Male",21,"ECE",4,7,7.9,88,"Placed","Salem","9876500003"),
    (4,"AIDS004","Meena","Lakshmi","Female",20,"AI&DS",3,5,9.2,96,"Placed","Karur","9876500004"),
    (5,"CSE005","Hari","Prasad","Male",22,"CSE",4,8,8.1,87,"Not Placed","Trichy","9876500005")
]

cursor.executemany("""
INSERT OR REPLACE INTO CollegeStudents
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
""", college_students)

# ==========================
# Insert Employees
# ==========================
employees = [
    (1,"EMP001","Ramesh","Kumar","Male",35,"HR","Manager",75000,95,"Chennai","9876600001"),
    (2,"EMP002","Suresh","Raj","Male",30,"IT","Developer",65000,92,"Madurai","9876600002"),
    (3,"EMP003","Anjali","Devi","Female",28,"Finance","Accountant",58000,90,"Salem","9876600003"),
    (4,"EMP004","Priya","Sharma","Female",32,"Marketing","Executive",62000,88,"Coimbatore","9876600004"),
    (5,"EMP005","Karthik","Mani","Male",29,"IT","Software Engineer",70000,96,"Karur","9876600005")
]

cursor.executemany("""
INSERT OR REPLACE INTO Employees
VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
""", employees)

conn.commit()
conn.close()

print("Database Created Successfully!")