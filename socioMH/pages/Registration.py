import streamlit as st
import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = " " # i cant provide this information for my privacy sake 
DB_HOST = "localhost"
DB_PORT = "5432"

st.markdown("""
    <style>
        .main {
           background: #000000;
           background: radial-gradient(at left top, #000000, #000000);

           opacity: 0.8;  
        }
        
         /* Change the sidebar color */
        .sidebar .sidebar-content {
            background-color: green;
        }
        .reportview-container .main .block-container {
            background-color: black;
        }
            
        /* Change the placeholder color */
        .stTextInput input {
            background-color: dark-grey;
        }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 9])
with col1:
    st.image("pages\img\Logo.png", width=100)
with col2:
    st.title("Social Medial Mental Health Assessment(M-Check)")
st.write("---")

def register_user(username, first_name, last_name, email, password):
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cursor = connection.cursor()

        # Insert user data into the "users" table
        insert_query = "INSERT INTO users (username, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(insert_query, (username, first_name, last_name, email, password))

        connection.commit()
        cursor.close()
        connection.close()

        st.success("Registration successful!")
    except Exception as e:
        st.error("Error: {}".format(e))



# page_selection == register_page:
st.info("### Register")
with st.form(key="registration_form"):
    new_username = st.text_input("New Username")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email Address")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    register_button = st.form_submit_button("Register")

    if new_password != confirm_password:
        st.error("Passwords do not match. Please try again.")
    elif register_button:
        register_user(new_username, first_name, last_name, email, new_password)
