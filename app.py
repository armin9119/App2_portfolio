import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title('Armin')
    content = """My name is Armin and I’m 14 years old. I just started learning programming and I’m really eager to improve. 
    I enjoy creating small projects and getting better every day. I like solving problems and taking on coding challenges.
    My goal is to grow in the world of programming and gain new experiences.
    """
    st.write(content)
