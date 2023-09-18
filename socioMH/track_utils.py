import psycopg2
from psycopg2 import sql

# Global connection and cursor objects
conn = psycopg2.connect(
    dbname="mcheck",
    user="postgres",
    password="nnedinma",
    host="localhost",
    port="5432"
)
c = conn.cursor()

def create_page_visited_table():
    c.execute("""
        CREATE TABLE IF NOT EXISTS pageVisitedTable (
            pagename TEXT NOT NULL,
            timeOfVisit TIMESTAMP NOT NULL
        )
    """)
    conn.commit()

def add_page_visited_details(pagename, timeOfVisit):
    c.execute("INSERT INTO pageVisitedTable (pagename, timeOfVisit) VALUES (%s, %s)", (pagename, timeOfVisit))
    conn.commit()

def view_all_page_visited_details():
    c.execute("SELECT * FROM pageVisitedTable")
    data = c.fetchall()
    return data

def create_emotionclf_table():
    c.execute("""
        CREATE TABLE IF NOT EXISTS emotionclfTable (
            rawtext TEXT NOT NULL,
            prediction TEXT NOT NULL,
            probability REAL NOT NULL,
            timeOfVisit TIMESTAMP NOT NULL
        )
    """)
    conn.commit()

def add_prediction_details(rawtext, prediction, probability, timeOfVisit):
    c.execute("INSERT INTO emotionclfTable (rawtext, prediction, probability, timeOfVisit) VALUES (%s, %s, %s, %s)", (rawtext, prediction, probability, timeOfVisit))
    conn.commit()

def view_all_prediction_details():
    c.execute("SELECT * FROM emotionclfTable")
    data = c.fetchall()
    return data
