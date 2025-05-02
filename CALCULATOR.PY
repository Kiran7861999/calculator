import streamlit as st

# Title
st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

# Select operation
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform calculation
result = None
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Cannot divide by zero")

# Display result
if result is not None:
    st.success(f"Result: {result}")
