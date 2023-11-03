import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

#Upload file
file = st.file_uploader("Upload your file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    # Add a slider to control number of rows
    n_rows = st.slider("Choose number of rows", min_value=3, max_value=len(df), step=1)

    # Choose specific columns --> df.columns to show all columns and transfert it to list
    n_columns = st.multiselect("Select columns", df.columns.to_list(), default=df.columns.to_list())

    #Print the table
    st.write(df[:n_rows][n_columns])

    # Show Tabs
    tab1, tab2, tab3 = st.tabs(["Scatter", "Histogram", "PieChart"])
    numerical_columns = df.select_dtypes(include=np.number).columns.to_list()

    #Scatter
    with tab1:
        col1, col2, col3 = st.columns(3)
        with col1:
            x_column = st.selectbox("Select feature on X axis", list(df.columns))
        with col2:
            y_column = st.selectbox("Select features on Y axis", list(df.columns))
        with col3:
            colors = st.selectbox("Select column as color", list(df.columns))

        fig_scatter = px.scatter(df, x=x_column, y=y_column, color=colors)
        st.plotly_chart(fig_scatter)

    #Histogram
    with tab2:
        histogram_feature = st.selectbox("Select feature", numerical_columns)
        fig_histogram = px.histogram(df, x=histogram_feature)
        st.plotly_chart(fig_histogram)
    
    with tab3:
        barchart_xaxis = st.selectbox("Select features as X axis", list(df.columns))
        barchart_yaxis = st.selectbox("Select features as Y axis", list(df.columns))
        fig_barchart = px.bar(df, x=barchart_xaxis, y=barchart_yaxis)
        st.plotly_chart(fig_barchart)
