from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide sql queries as response

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns:
    - NAME: The name of the student (string)
    - CLASS: The class the student is enrolled in (string)
    - SECTION: The section of the class (string)
    - MARKS: The marks obtained by the student (integer)

    Your task is to convert any English question into a valid SQL query that retrieves the required information from the STUDENT table.

    Examples:
    1. Question: How many students are in the Data Science class?
       SQL: SELECT COUNT(*) FROM STUDENT WHERE CLASS = 'Data Science';

    2. Question: Who are the students in section A?
       SQL: SELECT NAME FROM STUDENT WHERE SECTION = 'A';

    3. Question: What is the average marks of students in the DEVOPS class?
       SQL: SELECT AVG(MARKS) FROM STUDENT WHERE CLASS = 'DEVOPS';

    4. Question: List all students and their marks.
       SQL: SELECT NAME, MARKS FROM STUDENT;

    5. Question: How many students scored more than 80 marks?
       SQL: SELECT COUNT(*) FROM STUDENT WHERE MARKS > 80;

    Ensure the SQL query is syntactically correct and retrieves the required information accurately. Do not include any unnecessary formatting or keywords like `sql` in the output.
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)

# Function to list available models

def list_available_models():
    models = genai.list_models()
    for model in models:
        print("Model Attributes:")
        for attr, value in model.__dict__.items():
            print(f"{attr}: {value}")

# Call this function to see available models
list_available_models()

# Add Streamlit UI for database operations

st.sidebar.header("Database Operations")
operation = st.sidebar.selectbox("Choose an operation", ["Insert", "Update", "Delete", "View All"])

if operation == "Insert":
    st.subheader("Insert a New Record")
    name = st.text_input("Name", key="insert_name")
    class_name = st.text_input("Class", key="insert_class")
    section = st.text_input("Section", key="insert_section")
    marks = st.number_input("Marks", min_value=0, max_value=100, step=1, key="insert_marks")
    if st.button("Insert Record", key="insert_button"):
        from sql import insert_record
        insert_record(name, class_name, section, marks)
        st.success("Record inserted successfully!")

elif operation == "Update":
    st.subheader("Update an Existing Record")
    name = st.text_input("Name of the student to update", key="update_name")
    class_name = st.text_input("New Class (leave blank if no change)", key="update_class")
    section = st.text_input("New Section (leave blank if no change)", key="update_section")
    marks = st.number_input("New Marks (leave blank if no change)", min_value=0, max_value=100, step=1, value=0, key="update_marks")
    if st.button("Update Record", key="update_button"):
        from sql import update_record
        update_record(name, class_name if class_name else None, section if section else None, marks if marks else None)
        st.success("Record updated successfully!")

elif operation == "Delete":
    st.subheader("Delete a Record")
    name = st.text_input("Name of the student to delete", key="delete_name")
    if st.button("Delete Record", key="delete_button"):
        from sql import delete_record
        delete_record(name)
        st.success("Record deleted successfully!")

elif operation == "View All":
    st.subheader("All Records")
    from sql import fetch_all_records
    records = fetch_all_records()
    for record in records:
        st.write(record)