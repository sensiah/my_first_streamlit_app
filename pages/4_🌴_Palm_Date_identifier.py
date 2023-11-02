import streamlit as st
import time


#Title and Overview
st.markdown("<h1 style='text-align: center; '>Varieties of Dates</h1>", unsafe_allow_html=True)
st.write("The presentation below is an introduction the varieties of dates in Algeria and their distribution according to regions of production, in addition to information about the amount of production and export...etc.")

#Add the presentation from google Docs
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQx4f3CC651oqTXrYihiYWno4LxbkLmHHVJ01QAcbwMXThJyNvcWEAzvimNSo3_Ow/embed?start=false&loop=false&delayms=3000", height=565)

#Upload A date variety 
st.title("Check your date varity by uploding an image")
file = st.file_uploader("Please Enter your palm date", type=["jpg"])

if file is not None:
    st.write("أضرب دورة وأرواح 😂😁😂")
    time.sleep(2)
    st.write("Until I learn Machine Learning 😁")
