import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Rohit Singh")
    content = """
    Hi My name is Rohit Singh. Ik'm a Student a BCA student
     and I have Knowledge about Python and C++.
     I'm still a learner and I am Progressing very fast.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to Contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])