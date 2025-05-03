import streamlit as st
import random

# Set a secret number if not already set
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

# Set a counter for attempts
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# App title
st.title("🎯 Guess the Number Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check the guess
if st.button("Guess"):
    st.session_state.attempts += 1
    secret = st.session_state.secret_number

    if guess < secret:
        st.warning("Too low! Try again.")
    elif guess > secret:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
        if st.button("Play Again"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
