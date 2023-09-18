import streamlit as st
import psycopg2
from streamlit_extras.switch_page_button import switch_page


# st.write('Hi there this is the login page')

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "nnedinma"
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

def login_user(username, password):
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        cursor = connection.cursor()

        # Check if the provided username and password match a record in the "users" table
        select_query = "SELECT id FROM users WHERE username=%s AND password=%s;"
        cursor.execute(select_query, (username, password))
        user_id = cursor.fetchone()

        cursor.close()
        connection.close()

        if user_id:
            
            st.success(f"Logged In Successfully as {username}:")
            st.session_state.logged_in = True
            return True
        else:
            st.error("Invalid username or password.")
            return False
    except Exception as e:
        st.error("Error: {}".format(e))
        return False


    
if st.sidebar.button("Log Out"):
    st.session_state['logged_in'] = False  # Reset logged_in flag
    st.info("Successfully logged out.")  # Displaying log out success message
    st.experimental_rerun()  # Rerun the app to show login form
if 1 > 5:
    print('Hello')
else:
    st.info(" ### User Login")
    with st.form(key="login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Log in")
            
        

        if login_button:
            if login_user(username, password):
                print('Yes it passed')
                st.session_state['username'] = username  # Store username in session state
                st.session_state['logged_in'] = True     # Set logged_in flag
                switch_page("Analysis")  
                st.experimental_rerun()  # Rerun the app to hide login form
                
    # Show a logout success message after logging out
    if 'logged_out' in st.session_state and st.session_state['logged_out']:
        st.success("Logged out successfully!")
        del st.session_state['logged_out']

center_button = st.button('Back')
if center_button:
    switch_page("home")
