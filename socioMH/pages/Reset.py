

import streamlit as st
import psycopg2
from streamlit_extras.switch_page_button import switch_page

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

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "nnedinma"
DB_HOST = "localhost"
DB_PORT = "5432"


# Function to reset password
def reset_password(username, new_password):
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cursor = connection.cursor()

        # Update the user's password in the "users" table
        update_query = "UPDATE users SET password = %s WHERE username = %s;"
        cursor.execute(update_query, (new_password, username))

        connection.commit()
        cursor.close()
        connection.close()

        st.success("Password reset successful!")
    except Exception as e:
        st.error("Error: {}".format(e))

# elif page_selection == password_reset_page:
st.info("### Password Reset")
with st.form(key="password_reset_form"):
    username = st.text_input("Username")
    old_password = st.text_input("Old Password", type="password")
    new_password = st.text_input("New Password", type="password")
    confirm_new_password = st.text_input("Confirm New Password", type="password")
    reset_button = st.form_submit_button("Reset Password")

    if reset_button:
        if new_password != confirm_new_password:
            st.error("New passwords do not match. Please try again.")
        else:
            # Check if the old password matches the user's current password in the database
            if login_user(username, old_password):
                reset_password(username, new_password)
