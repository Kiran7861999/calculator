# import streamlit as st
# st.title("CAlculator appss")
# # Input numbers
# st.write ("Testing streamlit")
# num1 = st.number_input("Enter first number", format="%.2f")
# num2 = st.number_input("Enter second number", format="%.2f")
# st.write(f'the addition is {num1+num2}')
import streamlit as st

# Initialize session state for storing books
if "books" not in st.session_state:
    st.session_state.books = []

# App title
st.title("📚 Simple Book Store")

# Tabs for navigation
tab = st.radio("Navigate", ["Add Book", "View Books", "Search Book"])

# Add Book
if tab == "Add Book":
    st.header("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
    
    if st.button("Add Book"):
        if title and author:
            st.session_state.books.append({"title": title, "author": author, "price": price})
            st.success("Book added successfully!")
        else:
            st.warning("Please fill in all fields.")

# View Books
elif tab == "View Books":
    st.header("📖 All Books")
    if st.session_state.books:
        for idx, book in enumerate(st.session_state.books, start=1):
            st.markdown(f"**{idx}. {book['title']}** by {book['author']} - ${book['price']:.2f}")
    else:
        st.info("No books in the store yet.")

# Search Book
elif tab == "Search Book":
    st.header("🔍 Search Book by Title")
    query = st.text_input("Enter title keyword")
    if query:
        results = [book for book in st.session_state.books if query.lower() in book['title'].lower()]
        if results:
            for book in results:
                st.markdown(f"**{book['title']}** by {book['author']} - ${book['price']:.2f}")
        else:
            st.warning("No matching books found.")
