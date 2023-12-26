import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    row_message = f"""\
Subject: New email form :{user_email}
From: {user_email}
{message}
"""
    button = st.form_submit_button("Sumbit")
    print(button)
    if button:
       send_email(row_message)
       st.info("Your email is Send Successfully")
