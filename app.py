import streamlit as st

st.title("Welcome to Portfolio Flash!")
st.markdown("Here, you can build custom portfolios in a flash.")
st.write(" ")
firstName = st.text_input(label("What is your first name?"), "First name")
lastName = st.text_input(label("What is your last name?"), "Last name")