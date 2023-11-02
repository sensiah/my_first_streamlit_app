import streamlit as st
import time


file = st.file_uploader("Please Enter your palm date", type=["jpg"])

if file is not None:
    st.write("أضرب دورة وأرواح 😂😁😂")
    time.sleep(2)
    st.write("Until I learn Machine Learning 😁")
