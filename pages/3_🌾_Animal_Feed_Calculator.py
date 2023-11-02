import streamlit as st



#Title and Overview
st.markdown("<h1 style='text-align: center; '>Animal Feed Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>حاسبة العليقة</h1>", unsafe_allow_html=True)


farm_animals = ["🐪 إبل", "🐑 أغنام", "🐄 أبقار"]
selected_animal = st.selectbox("Choose Your Farm Animal (اختر نوع حيوان المزرعة)", options=farm_animals)

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
