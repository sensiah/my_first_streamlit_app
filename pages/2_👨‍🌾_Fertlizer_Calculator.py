import streamlit as st



#Title and Overview
st.markdown("<h1 style='text-align: center; '>Fertilization calculator</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>حاسبة التسميد</h1>", unsafe_allow_html=True)


fertilizer_type = st.selectbox("Choose the fertilizer type (أختر نوع السماد)", ["سماد مركب (NPK)", "سماد عادي"])

col1, col2, col3 = st.columns(3)

#Choose fertilizer type
if fertilizer_type == "سماد مركب (NPK)":
    pass
else:
    with col1:
        #available_fertilizer = st.number_input("السماد المتوفر", min_value=1)
        fertilizer_options = ("يوريا 46", "سوبرفوسفات")
        selected_fertilizer = st.selectbox("أختر نوع السماد", options=fertilizer_options)
        if selected_fertilizer == "سوبرفوسفات":
            pass
        else:
           available_fertilizer = 46 
    with col2:
        fertilizer_units = st.number_input("أدخل عدد وحدات السماد المراد إضافته", min_value=0, step=1)
    with col3:
        area = st.number_input("أدخل المساحة المغروسة بالمتر", min_value=0)

    fertilizer_quantity = ((fertilizer_units*100/available_fertilizer)*area/10000)

calcultor_button = st.button("أحسب")
if calcultor_button:
    st.write("وزن السماد: ", fertilizer_quantity)
