import streamlit as st
import re

st.title("Cyber Security Awareness Platform")

st.header("Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search("[A-Z]", password):
        score += 1

    if re.search("[a-z]", password):
        score += 1

    if re.search("[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score <= 2:
        st.error("Weak Password")

    elif score <= 4:
        st.warning("Medium Password")

    else:
        st.success("Strong Password")
