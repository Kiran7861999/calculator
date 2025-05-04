
import streamlit as st
import random

# Initialize session state
if 'positions' not in st.session_state:
    st.session_state.positions = {'Player 1': 0, 'Player 2': 0}
if 'turn' not in st.session_state:
    st.session_state.turn = 'Player 1'
if 'winner' not in st.session_state:
    st.session_state.winner = None

# Title
st.title("🎲 Simple Ludo Game")

# Display current positions
st.subheader("Token Positions")
for player, pos in st.session_state.positions.items():
    st.text(f"{player}: {pos}")

# Roll dice
if not st.session_state.winner:
    st.subheader(f"{st.session_state.turn}'s Turn")
    if st.button("Roll Dice"):
        roll = random.randint(1, 6)
        st.write(f"🎲 {st.session_state.turn} rolled a {roll}!")

        # Update position
        st.session_state.positions[st.session_state.turn] += roll
        if st.session_state.positions[st.session_state.turn] >= 30:
            st.session_state.winner = st.session_state.turn
        else:
            # Switch turn
            st.session_state.turn = 'Player 2' if st.session_state.turn == 'Player 1' else 'Player 1'

# Show winner
if st.session_state.winner:
    st.success(f"🏆 {st.session_state.winner} wins!")

# Reset game
if st.button("🔄 Restart Game"):
    st.session_state.positions = {'Player 1': 0, 'Player 2': 0}
    st.session_state.turn = 'Player 1'
    st.session_state.winner = None
