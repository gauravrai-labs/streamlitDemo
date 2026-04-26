import streamlit as st
import requests

st.title("Currency Converter")
st.subheader("Convert currency using ExchangeRate-API")
st.text_input("Enter the amount to convert", key="amount")
st.selectbox("Select the currency to convert from", ["USD", "EUR", "GBP", "INR"], key="from_currency")
st.selectbox("Select the currency to convert to", ["USD", "EUR", "GBP", "INR"], key="to_currency")
if st.button("Convert"):
    amount = st.session_state.amount
    from_currenct = st.session_state.from_currency
    to_currency = st.session_state.to_currency
    if not amount : 
        st.warning("Please enter the amount to convert.")
    elif from_currenct == to_currency:
        st.warning("Please select different currencies to convert.")
    else:
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currenct}&to={to_currency}"
        response = requests.get(url)
        if response.status_code == 200:
            response_dict = (response.json())
            converted_amount = response_dict["rates"][to_currency]
            st.success(f"{amount} {from_currenct} is equal to {converted_amount} {to_currency}.")
        else:
            st.error("Failed to fetch exchange rate. Please try again later.")  
            