Natural Language to SQL Query Conversion

Uses Google’s Gemini-Pro model to generate SQL queries from English questions.
Ensures query accuracy by providing a structured prompt with examples.
Database Query Execution

Queries are executed on an SQLite database (student.db).
Supports operations like counting entries, filtering by class, and retrieving student details.
Streamlit-based Web UI

Users enter questions in plain English via a simple and interactive UI.
The app displays SQL results after query execution.
Secure API and Database Access

Loads the Google API Key from a .env file for security.
Uses SQLite as a lightweight, local database solution.
Technologies Used:
Google Generative AI (gemini-pro) – For SQL query generation.
SQLite – For database storage and queries.
Streamlit – For the web interface.
Dotenv – For securely managing API keys.
Python – For handling AI interactions and database execution.
