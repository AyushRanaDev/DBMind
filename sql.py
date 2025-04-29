import sqlite3

# Add modular functions for database operations

def insert_record(name, class_name, section, marks):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)", (name, class_name, section, marks))
    connection.commit()
    connection.close()

def update_record(name, class_name=None, section=None, marks=None):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    if class_name:
        cursor.execute("UPDATE STUDENT SET CLASS = ? WHERE NAME = ?", (class_name, name))
    if section:
        cursor.execute("UPDATE STUDENT SET SECTION = ? WHERE NAME = ?", (section, name))
    if marks:
        cursor.execute("UPDATE STUDENT SET MARKS = ? WHERE NAME = ?", (marks, name))
    connection.commit()
    connection.close()

def delete_record(name):
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM STUDENT WHERE NAME = ?", (name,))
    connection.commit()
    connection.close()

def fetch_all_records():
    connection = sqlite3.connect("student.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    rows = cursor.fetchall()
    connection.close()
    return rows