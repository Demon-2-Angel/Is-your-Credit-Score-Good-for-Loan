import os
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load the dataset for fitting the encoder and scaler
data_path = r'credit_scoring_dataset_large.xlsx'
df = pd.read_excel(data_path)

# Define categorical and numerical features
categorical_features = ['payment_history', 'credit_mix', 'job_stability', 'industry_stability', 'utility_bills_payment_history']
numerical_features = ['late_payments', 'bankruptcies', 'credit_utilization', 'outstanding_balances', 'oldest_account_age', 
                      'avg_account_age', 'recent_inquiries', 'employment_income', 'bonus_commission_income', 'outstanding_loans', 
                      'credit_card_balances']

# Fit the OneHotEncoder and StandardScaler with the original dataset
encoder = OneHotEncoder(sparse_output=False)  # Updated parameter
encoded_features = encoder.fit_transform(df[categorical_features])

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[numerical_features])

# Load the neural network model
model = load_model('credit_score_model.h5')

# Define the neural expert system function
def neural_expert_system(input_data):
    # Convert input_data to DataFrame to match the original dataset
    input_df = pd.DataFrame([input_data])

    # Preprocess the input data similarly to the training data
    encoded_input = encoder.transform(input_df[categorical_features])
    scaled_input = scaler.transform(input_df[numerical_features])
    combined_input = np.hstack((encoded_input, scaled_input))
    
    # Predict the credit score using the neural network model
    predicted_score = model.predict(combined_input)
    return predicted_score[0][0]

# Example input data
input_data = {
    'payment_history': 'good',
    'late_payments': 1,
    'bankruptcies': 0,
    'credit_utilization': 20,
    'outstanding_balances': 1500,
    'oldest_account_age': 6,
    'avg_account_age': 5,
    'credit_mix': 'moderate',
    'recent_inquiries': 2,
    'employment_income': 60000,
    'bonus_commission_income': 5000,
    'job_stability': 'stable',
    'industry_stability': 'stable',
    'outstanding_loans': 10000,
    'credit_card_balances': 2000,
    'utility_bills_payment_history': 'good'
}

predicted_score = neural_expert_system(input_data)
print(f'Predicted Credit Score: {400+predicted_score}')
