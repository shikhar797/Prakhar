import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title="My Webpage",page_icon="🧑‍💼",layout="wide")



#--Header--

with st.container():
    text_column,image_column=st.columns((2,1))
    with text_column:
        st.subheader("Hi,I am Prakhar Gupta:wave:")
        st.title("A Engineer from India")
        st.write("I am passionate about Finance and i take intrest in Stock Market")
        st.write("[Learn more >](https://www.linkedin.com/in/prakhar-gupta-79836317a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app )")
    with image_column:
        st.image('output.png')   

def load_lottie(url):
    r=requests.get(url)
    return r.json()

lottie_finance=load_lottie("https://lottie.host/3117f0ed-7417-45e1-afcd-92b0475ec9cf/BjVuzIq8yf.json")
# --what i do--
with st.container():
    st.write("---")
left_column, right_column = st.columns(2)

# Content for the left column
with left_column:
    st.header("What I Do")
    st.write("######")  # Adds some spacing
    st.write(
        """
        - I am currently working with JSW Steel Karnataka, India as an Assistant Manager.
        - I have done a 6-month internship at Asahi India Glass Limited (AIS).
        - I have done two 2-month internships at VS ENVIROCARE PVT.LTD and at Perfect Techno Mech Industries.
        - I have also completed 2 courses in finance:
            1. Financial Modeling and Valuation from Internshala.
            2. Financial Reporting and Analysis from Udemy.
        """
    )
    st.write("[LinkedIn >](https://www.linkedin.com/in/prakhar-gupta-79836317a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")

# Content for the right column
with right_column:
    st_lottie(lottie_finance, height=300, width=300)