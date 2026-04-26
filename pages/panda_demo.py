import streamlit as st
import pandas as pd

st.title("Pandas DataFrame in Streamlit")
st.subheader("Displaying a DataFrame using Streamlit")

df = pd.DataFrame()
file = st.file_uploader("Upload a CSV file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    #st.write(df)
    selected_column = st.selectbox("Select a column to display", df.columns)
    submitted = st.button("Submit")
    if submitted:
        st.write(df[[selected_column]])