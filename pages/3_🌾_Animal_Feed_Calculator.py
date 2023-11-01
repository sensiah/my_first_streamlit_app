import streamlit as st



st.header("حاسبة العليقة")
st.header("Animal Feed Calculator")

farm_animals = ["🐪 إبل", "🐑 أغنام", "🐄 أبقار"]
selected_animal = st.selectbox("اختر نوع الحيوان", options=farm_animals)

if selected_animal == "🐪 إبل":
    pass
elif selected_animal == "🐄 أبقار":
    weight = st.number_input("الوزن",step=1)
    age = st.number_input("العمر بالأشهر",step=1)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("عليقة الحفاظ")
        st.write("MAD: ")
        st.write("Vitamin: ")

    with col2:
        st.subheader("عليقة الإنتاج")
        st.write("MAD: ")
        st.write("Vitamin: ")    
    
    st.subheader("العليقة الكلية")