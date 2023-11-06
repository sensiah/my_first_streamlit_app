import streamlit as st
import streamlit.components.v1 as components
from streamlit_carousel import carousel
import time

import streamlit as st

#Title and Overview
st.markdown("<h1 style='text-align: center; '>Varieties of Dates</h1>", unsafe_allow_html=True)
st.write("The presentation below is an introduction the varieties of dates in Algeria and their distribution according to regions of production, in addition to information about the amount of production and export...etc.")

#Add the presentation from google Docs
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQx4f3CC651oqTXrYihiYWno4LxbkLmHHVJ01QAcbwMXThJyNvcWEAzvimNSo3_Ow/embed?start=false&loop=false&delayms=3000", height=565)

#Here th photo slider
st.markdown("<h1 style='text-align: center; '>Here Some Varities of Dates</h1>", unsafe_allow_html=True)
photo_slider = [
    dict(
        title="دقلــة نــور",
        text="تعتبر من أجود أنواع التمور في العــالم",
        img="https://upload.wikimedia.org/wikipedia/commons/a/a2/Dattes_deglet_from_Biskra.jpg",
    ),
    dict(
        title="الغـــرس",
        text="ثـــاني أشهر صنف في الجزائر",
        img="https://scontent.forn2-1.fna.fbcdn.net/v/t1.6435-9/41754844_2136508239949668_7610823292806496256_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=84c479&_nc_ohc=Ms95DRThzxEAX9vVHN_&_nc_ht=scontent.forn2-1.fna&oh=00_AfD9pK6YgkMiSZF4MiAMC3xJY6-qhI0t-CepvYcR5rLKsA&oe=656B1FA8",
    ),
    dict(
        title="الحمــيرة",
        text="أهم الأصناف المنتجة في الجنوب الغربي والتي توجه للمقايضة",
        img="https://pbs.twimg.com/media/EePSapiXoAE_WsG?format=jpg&name=large",
    ),
]
carousel(items=photo_slider, width=1)

#Upload A date variety 
st.title("Check your date varity by uploding an image")
file = st.file_uploader("Please Enter your palm date", type=["jpg"])

if file is not None:
    st.write("أضرب دورة وأرواح 😂😁😂")
    time.sleep(2)
    st.write("Until I learn Machine Learning 😁")
