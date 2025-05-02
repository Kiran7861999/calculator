import streamlit as st

# App title
st.title("🔢 Even or Odd Checker")

# Input number
number = st.number_input("Enter an integer", step=1)

# Check if number is even or odd
if st.button("Check"):
    if number % 2 == 0:
        st.success(f"{int(number)} is Even ✅")
    else:
        st.info(f"{int(number)} is Odd 🔵")
