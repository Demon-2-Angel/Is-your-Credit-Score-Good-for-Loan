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

# Load the model for future predictions
def load_neural_expert_system_model():
    global model, encoder, scaler
    model = load_model('credit_score_model.h5')

# Use the loaded model
load_neural_expert_system_model()

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

# Get the predicted score from the neural expert system
predicted_score = neural_expert_system(input_data)
print(f'Predicted Credit Score: {predicted_score}')