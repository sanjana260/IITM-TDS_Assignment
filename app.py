import streamlit as st
st.write("""
# Graded Assignment 8
By Sanjana Mohan for Tools in Data Science
""")
st.header("Please Enter 3 Numbers")

a = st.number_input("A")
b = st.number_input("B")
c = st.number_input("C")

st.subheader("Largest Value")
st.write(f"The largest value is : {max(a,b,c)}")