from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text.strip()


##Function to retrieve query from the sql database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = [
        """
        You are an expert in converting English questions to SQL Queries.
        The SQL database is named 'STUDENT' and has the following columns: NAME, CLASS, SECTION, and MARKS.
        Examples:
        1. How many entries of records are present?
        SQL: SELECT COUNT(*) FROM STUDENT;
        2. Tell me all the students studying in Data Science class.
        SQL: SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
        Provide only the SQL query without any additional text or explanation.
        """
]

st.set_page_config(page_title = "I can retrieve any SQL query")
st.header("Gemini app to retrieve SQL Data")
question = st.text_input("Input:",key = "input")
submit = st.button("Ask the question")
if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,"student.db")
    st.subheader("the response is")
    for row in response:
        print(row)
        st.write(row)