# name = input("Enter student name> ")
# roll_number = int(input("Enter roll number> "))
# math = float(input("Enter marks for math> "))
# english = float(input("Enter marks for english> "))
# computer = float(input("Enter marks for computer> "))
# total = math + computer + english
# percentage = (total / 300) * 100
# if percentage >= 90:
#     grade = 'A+'
# elif percentage >= 80:
#     grade = 'A'
# elif percentage >= 70:
#     grade = 'B'
# elif percentage >= 60:
#     grade = 'C'
# elif percentage >= 50:
#     grade = 'D'
# else:
#     grade = 'F'
# print("name:", name)
# print("roll No:",roll_number)
# print("math:",math)
# print("computer:",computer)
# print("english:",english)
# print("total:",total)
# print("percentage :",percentage)
# print("grade:", grade)
import streamlit as st

# App title
st.title("📄 Student Marksheet Generator")

# Student Details
st.header("🧑‍🎓 Student Information")
name = st.text_input("Student Name")
roll_no = st.text_input("Roll Number")

# Marks Input
st.header("📝 Enter Marks (Out of 100)")
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = {}

for subject in subjects:
    marks[subject] = st.number_input(f"{subject} Marks", min_value=0, max_value=100, step=1)

# Calculate and Display Results
if st.button("Generate Marksheet"):
    if not name or not roll_no:
        st.warning("Please fill in all student details.")
    else:
        total = sum(marks.values())
        average = total / len(subjects)

        # Grade Calculation
        if average >= 90:
            grade = "A+"
        elif average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "F"

        # Display Marksheet
        st.subheader("📊 Marksheet")
        st.write(f"**Name:** {name}")
        st.write(f"**Roll No:** {roll_no}")
        st.write("---")
        for subject, mark in marks.items():
            st.write(f"**{subject}:** {mark} / 100")
        st.write("---")
        st.write(f"**Total Marks:** {total} / 500")
        st.write(f"**Average:** {average:.2f}")
        st.write(f"**Grade:** {grade}")
