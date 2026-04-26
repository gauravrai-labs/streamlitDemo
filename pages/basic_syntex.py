import streamlit as st

st.title("Hello, Streamlit!")
st.subheader("Welcome to my Streamlit app.")
st.write("This is a simple Streamlit components test app.")

name = st.text_input("Enter your name")
age = st.number_input("Enter you age number", min_value=18, max_value=100,value=18)
dob = st.date_input("Enter your date of birth", value=None, min_value=None, max_value=None, key=None)
city = st.selectbox("select your city", ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"])
temp = st.slider("select temperature", -10, 40, 20)
terms = st.checkbox("I agree to the terms and conditions")

button_clicked = st.button("Submit")
if button_clicked:
    if terms:
        st.success(f"hello {name}, you are {age} years old.")
        st.success(f"You have selected {city} with a temperature of {temp}°C.")
    else:
        if not city:
            st.warning("Please select a city.")
        if not name:
            st.warning("Please enter your name.")
        if not age:
            st.warning("Please enter your age.")
        if not terms:
            st.warning("Please agree to the terms and conditions.")


