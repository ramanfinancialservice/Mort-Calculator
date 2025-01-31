
import streamlit as st
import numpy as np

def calculate_mortgage(loan_amount, years, rate):
    months = years * 12
    monthly_rate = rate / 100 / 12
    monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    total_interest = (monthly_payment * months) - loan_amount
    return monthly_payment, total_interest

# Streamlit Web App
st.title("Mortgage Comparison Calculator")

# User Inputs
loan_amount = st.number_input("Loan Amount ($):", min_value=10000, step=5000, value=500000)
loan_term = st.number_input("Loan Term (Years):", min_value=1, max_value=40, value=25)
rate1 = st.number_input("Mortgage 1 Interest Rate (%):", min_value=0.1, max_value=20.0, value=3.5)
rate2 = st.number_input("Mortgage 2 Interest Rate (%):", min_value=0.1, max_value=20.0, value=4.2)

if st.button("Compare Mortgages"):
    # Calculate Mortgage Payments
    payment1, interest1 = calculate_mortgage(loan_amount, loan_term, rate1)
    payment2, interest2 = calculate_mortgage(loan_amount, loan_term, rate2)

    # Display Results
    st.write(f"### Mortgage 1")
    st.write(f"**Monthly Payment:** ${payment1:.2f}")
    st.write(f"**Total Interest Paid:** ${interest1:.2f}")

    st.write(f"### Mortgage 2")
    st.write(f"**Monthly Payment:** ${payment2:.2f}")
    st.write(f"**Total Interest Paid:** ${interest2:.2f}")

    interest_savings = interest2 - interest1
    st.write(f"### Interest Savings with Mortgage 1: **${interest_savings:.2f}**")
