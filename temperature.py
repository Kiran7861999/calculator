import streamlit as st

# App title
st.title("🌡️ Temperature Converter (Celsius ↔ Fahrenheit)")

# Select conversion direction
conversion = st.radio("Select conversion direction:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

# Input temperature
temp_input = st.number_input("Enter the temperature:", format="%.2f")

# Conversion logic
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# Convert and display result
if st.button("Convert"):
    if conversion == "Celsius to Fahrenheit":
        result = c_to_f(temp_input)
        st.success(f"{temp_input:.2f}°C = {result:.2f}°F")
    else:
        result = f_to_c(temp_input)
        st.success(f"{temp_input:.2f}°F = {result:.2f}°C")
