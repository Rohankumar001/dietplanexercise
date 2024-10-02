import streamlit as st

# Function to recommend a single exercise based on user inputs
def recommend_exercise(age, gender, height, weight):
    bmi = (weight / ((height / 100) ** 2))  # Calculate BMI
    
    # Logic for exercise recommendation based on BMI and other factors
    if bmi >= 30:
        if age <= 40:
            return "Running"
        elif 40 < age <= 60:
            return "Cycling"
        else:
            return "Swimming"
    elif 25 <= bmi < 30:
        if gender == "Male":
            return "Jogging"
        else:
            return "Brisk Walking"
    elif 18.5 <= bmi < 25:
        if height > 170:
            return "Yoga"
        else:
            return "Pilates"
    else:
        if weight < 50:
            return "Weightlifting"
        else:
            return "Calisthenics"

# Streamlit App UI
st.title('💪 Diet Plan & Exercise Recommendation System 🏋️‍♀️')

# Sidebar for user inputs
st.sidebar.header('Input Your Details:')
age = st.sidebar.number_input('Enter your Age', min_value=10, max_value=100, step=1)
gender = st.sidebar.selectbox('Select your Gender', ['Male', 'Female', 'Other'])
height = st.sidebar.number_input('Enter your Height (in cm)', min_value=100, max_value=250, step=1)
weight = st.sidebar.number_input('Enter your Weight (in kg)', min_value=30, max_value=200, step=1)

# Button to trigger exercise recommendation
if st.sidebar.button('Recommend Exercise 🏃‍♂️'):
    exercise = recommend_exercise(age, gender, height, weight)
    
    # Format the result in a more visually appealing way
    st.markdown(
        f"<div style='text-align: center; font-size: 24px; font-weight: bold; color: #2c3e50;'>"
        f"Your recommended exercise is: "
        f"<span style='color: #e74c3c;'>{exercise}</span>"
        f"</div>",
        unsafe_allow_html=True
    )

# Optional BMI display
bmi = weight / ((height / 100) ** 2)
st.sidebar.write(f"Your BMI: {bmi:.2f}")
