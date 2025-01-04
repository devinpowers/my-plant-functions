import pyodbc
import os

def get_database_connection():
    connection_string = os.getenv("AZURE_SQL_CONNECTION_STRING")
    return pyodbc.connect(connection_string)

def get_due_plants():
    conn = get_database_connection()
    query = """
    SELECT id, name, contact_email
    FROM Plants
    WHERE DATEDIFF(day, last_watered, GETDATE()) >= reminder_days
    """
    cursor = conn.cursor()
    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    plants = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return plants
