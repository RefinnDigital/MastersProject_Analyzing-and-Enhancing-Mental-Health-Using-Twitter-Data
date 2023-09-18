# importing 
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64



# Home Page


st.set_page_config(
    page_title = "Social Medial Mental Health Assessment(M-Check)",
    initial_sidebar_state="collapsed",
    layout="wide"
    )

if 'logging_in' in st.session_state and st.session_state ['logging_in']:
    if st.sidebar.button ('Log Out'):
        st.session_state['logged_in'] = False  
        st.info("Successfully logged out.")  
        st.experimental_rerun()  

col1, col2 = st.columns([1, 9])
with col1:
    st.image("pages\img\Logo.png", width=100)
with col2:
    st.title("Social Media Mental Health Assessment(M-Check)")
st.write("---")
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        st.markdown(
     f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        max-width: 1800px;   
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('.\\pages\\img\\img.jpg')

st.markdown("""
    <style>
        .main {
           background: #000000;
           background: radial-gradient(at left top, #000000, #000000);

           opacity: 0.9;  
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


st.info(" ### Welcome to SocioMental_Check! 👋")



intro_text = """
Mental health is an increasingly critical concern in today's fast-paced world, and traditional methods of assessment often fall short in capturing the nuances of our psychological well-being. Leveraging the power of artificial intelligence and natural language processing, SocioMental_Check App aims to bridge this gap by unlocking the vast reservoir of information embedded in the tweets shared on one of the world's most influential social media platforms.     
"""
st.markdown('<div style="text-align: justify;">{}</div>'.format(intro_text), unsafe_allow_html=True)
st.write("#")
st.write("#")
col1, col2 = st.columns(2)
with col1:

    st.info(" Our App")
    intro_text2 = """
    Our app utilizes state-of-the-art algorithms to delve deep into the text of Twitter posts, seeking out subtle indicators and linguistic cues that hint at an individual's emotional state and mental health.
    By analyzing these patterns at scale, SocioMental_Check provides a comprehensive and real-time understanding of societal mental health trends.
    allowing mental health professionals, researchers, and policymakers to make informed decisions and interventions.
    """
    st.markdown('<div style="text-align: justify;">{}</div>'.format(intro_text2), unsafe_allow_html=True)

    

with col2:
    st.info(''' Let's End the Stigma Together!!!''')
    intro_text3 = """The intersection of social media and mental health is a delicate and ongoing area of research in our current digital era. The pervasive influence of social media has deeply permeated our lives, to the point where many individuals find themselves increasingly disconnected from real-world interactions with friends and family. This shift towards digital engagement can lead to feelings of depression, anxiety, sadness, fear, and loneliness.It's crucial to remember that social media is a tool that should be used mindfully. Regular breaks from these platforms can help maintain a healthy balance and prevent digital overload. Furthermore, it's important to keep in mind that the content we see on social media often represents a carefully curated highlight reel of someone's life, not their full reality.
    """
    st.markdown('<div style="text-align: justify;">{}</div>'.format(intro_text3), unsafe_allow_html=True)

    



col1, col2, col3 = st.columns(3)
with col2:
    center_button = st.button('Get Started')
    if center_button:
        switch_page("Log_in")



