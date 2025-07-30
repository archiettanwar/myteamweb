import streamlit as st
import pandas
from sendemail import sendemail

with st.form(key="sendemail"):
    st.title("Contact Page")
    senderemail=st.text_input("enter your email address")
    topics=pandas.read_csv("topics.csv")
    topic_of_user=st.selectbox("choose a topic:",topics["topic"])
    msg=st.text_area("enter your message.....")
    a=st.form_submit_button("submit")
    msg=(f"{topic_of_user}'\n'{msg}")
    if a:
        sendemail(senderemail,msg)
