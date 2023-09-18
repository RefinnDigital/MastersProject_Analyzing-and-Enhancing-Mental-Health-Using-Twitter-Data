import streamlit as st
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
    st.image("pages\img\Clinic.png", width=100)
with col2:
    st.title("Social Medial Mental Health Assessment(M-Check)")
st.write("---")

#  if page_selection == contact_page:
st.info("### Contact Us")
intro_text = """
For any enquiries or further information about our project on Social Media and Mental Health Analytics, please feel free to reach out.

Project Lead:
Jennifer Nneoma Shedrack
Student ID: 22168990
Email: [Jennifer.Shedrack@mail.bcu.ac.uk]

Project Supervisor: 
Dr. Mariam Adedoyin-Olowe
Senior Lecturer, Birmingham City University
Email: [Mariam.Adedoyin-Olowe@bcu.ac.uk]

We appreciate your interest in our work and look 
forward to hearing from you.
"""
st.markdown('<div style="text-align: justify;">{}</div>'.format(intro_text), unsafe_allow_html=True)
