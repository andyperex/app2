import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hi I am a guy
    and I am awesome
    and I want to learn something new
    and Joyce needs a shower.
    Precisa mais uma vez
    """
    st.info(content)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:20].iterrows():
        st.header(row["title"])