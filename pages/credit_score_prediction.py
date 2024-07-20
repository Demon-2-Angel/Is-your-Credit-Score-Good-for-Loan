import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model

def app():
    st.title('Credit Score Prediction')

    # Load the preprocessing objects
    with open('encoder.pkl', 'rb') as f:
        encoder = pickle.load(f)

    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    # Load the trained model
    model = load_model('credit_score_model2.h5')

    # Define the prediction function
    def neural_expert_system(input_data):
        input_df = pd.DataFrame([input_data])
        encoded_input = encoder.transform(input_df[categorical_features])
        scaled_input = scaler.transform(input_df[numerical_features])
        combined_input = np.hstack((encoded_input, scaled_input))
        predicted_score = model.predict(combined_input)
        return predicted_score[0][0]

    # Define categorical and numerical features
    categorical_features = ['payment_history', 'credit_mix', 'job_stability', 'industry_stability', 'utility_bills_payment_history']
    numerical_features = ['late_payments', 'bankruptcies', 'credit_utilization', 'outstanding_balances', 'oldest_account_age', 
                          'avg_account_age', 'recent_inquiries', 'employment_income', 'bonus_commission_income', 'outstanding_loans', 
                          'credit_card_balances']

    # Add input fields for user data in the sidebar
    st.sidebar.header('User Input Parameters')
    payment_history = st.sidebar.selectbox('Payment History', ['good', 'bad', 'average'])
    credit_mix = st.sidebar.selectbox('Credit Mix', ['moderate', 'low', 'high'])
    job_stability = st.sidebar.selectbox('Job Stability', ['stable', 'unstable'])
    industry_stability = st.sidebar.selectbox('Industry Stability', ['stable', 'unstable'])
    utility_bills_payment_history = st.sidebar.selectbox('Utility Bills Payment History', ['good', 'bad', 'average'])

    late_payments = st.sidebar.number_input('Late Payments', min_value=0, value=0)
    bankruptcies = st.sidebar.number_input('Bankruptcies', min_value=0, value=0)
    credit_utilization = st.sidebar.number_input('Credit Utilization (%)', min_value=0, value=20)
    outstanding_balances = st.sidebar.number_input('Outstanding Balances', min_value=0, value=1500)
    oldest_account_age = st.sidebar.number_input('Oldest Account Age (years)', min_value=0, value=6)
    avg_account_age = st.sidebar.number_input('Average Account Age (years)', min_value=0, value=5)
    recent_inquiries = st.sidebar.number_input('Recent Inquiries', min_value=0, value=2)
    employment_income = st.sidebar.number_input('Employment Income', min_value=0, value=60000)
    bonus_commission_income = st.sidebar.number_input('Bonus/Commission Income', min_value=0, value=5000)
    outstanding_loans = st.sidebar.number_input('Outstanding Loans', min_value=0, value=10000)
    credit_card_balances = st.sidebar.number_input('Credit Card Balances', min_value=0, value=2000)

    # Collect inputs
    input_data = {
        'payment_history': payment_history,
        'late_payments': late_payments,
        'bankruptcies': bankruptcies,
        'credit_utilization': credit_utilization,
        'outstanding_balances': outstanding_balances,
        'oldest_account_age': oldest_account_age,
        'avg_account_age': avg_account_age,
        'credit_mix': credit_mix,
        'recent_inquiries': recent_inquiries,
        'employment_income': employment_income,
        'bonus_commission_income': bonus_commission_income,
        'job_stability': job_stability,
        'industry_stability': industry_stability,
        'outstanding_loans': outstanding_loans,
        'credit_card_balances': credit_card_balances,
        'utility_bills_payment_history': utility_bills_payment_history
    }

    if st.sidebar.button('Predict'):
        predicted_score = neural_expert_system(input_data)
        predicted_score = round(predicted_score)
        st.markdown(f"<a name='result'></a>", unsafe_allow_html=True)  # Anchor to scroll to
        st.markdown(f'### Predicted Credit Score: {400 + predicted_score}', unsafe_allow_html=True)
        st.markdown("<script>window.location.href = '#result';</script>", unsafe_allow_html=True)
        st.balloons()
        
    # Limitations Section
    st.write("""
    ## Limitations of Each Parameter

    ### Payment History
    - **Limitation**: select the option that best describes your payment history for on-time payments.

    ### Credit Mix
    - **Limitation**: Defaults and bankruptcies are severe negative marks on your credit history. Enter the total number of bankruptcies you have had.

    ### Job Stability
    - **Limitation**: Weather his/her job is stable or not

    ### Industry Stability
    - **Limitation**: Weather his/her industry is stable or not
             
    ### Utility Bills Payment History
    - **Limitation**: Does he pay for the Utilities on time or not, what's the history ?
             
    ### Late Payments
    - **Limitation**: Any Late Payments uptill now ? 
             
    ### Bankruptcies
    - **Limitation**: Defaults and bankruptcies are severe negative marks on your credit history. Enter the total number of bankruptcies you have had.
             
    ### Credit Utilization
    - **Limitation**: How much in percentage does our user use in terms of credit utilization.

    ### Outstanding Balances
    - **Limitation**: How much he/she owes to the institutions

    ### Oldest Account Age
    - **Limitation**: What is his/her oldest account age in terms of years
             
    ### Average Account Age
    - **Limitation**: What is his/her average account age in terms of years
             
    ### Recent Inquiries
    - **Limitation**: How much he/she inquire ?
             
    ### Employment Income
    - **Limitation**: What is his/her income
             
    ### Bonus/Commission Income
    - **Limitation**: Amount of External Income
             
    ### Outstanding Loans
    - **Limitation**: Amount of Outstanding Loans
             
    ### Credit Card Balances
    - **Limitation**: What is his/her credit card balance in numbers ?
                 """)
    
    