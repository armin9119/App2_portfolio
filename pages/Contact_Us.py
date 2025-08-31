import streamlit as st
from send_email import send_email
st.title("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""
    Subject: New email
    
    From: armincook7@gmail.com
    To: {user_email}
    {raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_email, message)
        st.info("Email sent")
