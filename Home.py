import streamlit as st
import pandas as pd

# streamlit run Home.py
# http://localhost:8501

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png",)

with col2:
    st.title('Armin')
    content = """My name is Armin and I’m 14 years old. I just started learning programming and I’m really eager to improve. 
    I enjoy creating small projects and getting better every day. I like solving problems and taking on coding challenges.
    My goal is to grow in the world of programming and gain new experiences.
    """
    st.info(content)

content2 = """
Below you can find some of the apps i have built in python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col,col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[ :10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row['url']})')


with col4:
    for index, row in df[10:20].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row['url']})')
