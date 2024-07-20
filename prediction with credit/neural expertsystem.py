import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Load the dataset
data_path = r'credit_scoring_dataset_large.xlsx'
df = pd.read_excel(data_path)

# Define the function to calculate the credit score based on the expert system rules
def calculate_credit_score(row):
    credit_score = 0

    # Payment History - On-Time Payments
    if row['payment_history'] == 'excellent':
        credit_score += 100
    elif row['payment_history'] == 'good':
        credit_score += 80
    elif row['payment_history'] == 'fair':
        credit_score += 50
    elif row['payment_history'] == 'poor':
        credit_score += 20

    # Late Payments
    if row['late_payments'] == 0:
        credit_score += 30
    elif 1 <= row['late_payments'] <= 2:
        credit_score += 20
    elif 3 <= row['late_payments'] <= 4:
        credit_score += 10
    elif row['late_payments'] > 4:
        credit_score -= 20

    # Defaults and Bankruptcies
    if row['bankruptcies'] == 0:
        credit_score += 50
    elif row['bankruptcies'] == 1:
        credit_score -= 50
    elif row['bankruptcies'] > 1:
        credit_score -= 100

    # Amounts Owed - Credit Utilization Ratio
    if row['credit_utilization'] < 10:
        credit_score += 50
    elif row['credit_utilization'] < 30:
        credit_score += 30
    elif row['credit_utilization'] < 50:
        credit_score += 10
    elif row['credit_utilization'] > 50:
        credit_score -= 30

    # Amounts Owed - Outstanding Balances
    if row['outstanding_balances'] < 1000:
        credit_score += 20
    elif row['outstanding_balances'] < 5000:
        credit_score += 10
    elif row['outstanding_balances'] > 5000:
        credit_score -= 20

    # Length of Credit History - Age of Oldest Account
    if row['oldest_account_age'] > 10:
        credit_score += 40
    elif row['oldest_account_age'] > 5:
        credit_score += 20
    elif row['oldest_account_age'] < 3:
        credit_score += 10

    # Length of Credit History - Average Age of Accounts
    if row['avg_account_age'] > 7:
        credit_score += 30
    elif row['avg_account_age'] > 5:
        credit_score += 20
    elif row['avg_account_age'] < 3:
        credit_score += 10

    # Credit Mix - Types of Credit Accounts
    if row['credit_mix'] == 'diverse':
        credit_score += 20
    elif row['credit_mix'] == 'moderate':
        credit_score += 10
    elif row['credit_mix'] == 'limited':
        credit_score += 0

    # New Credit - Recent Credit Inquiries
    if row['recent_inquiries'] == 0:
        credit_score += 20
    elif row['recent_inquiries'] <= 2:
        credit_score += 10
    elif row['recent_inquiries'] > 2:
        credit_score -= 10

    # Income Levels - Employment Income
    if row['employment_income'] > 100000:
        credit_score += 50
    elif row['employment_income'] > 50000:
        credit_score += 30
    elif row['employment_income'] < 50000:
        credit_score += 10

    # Income Levels - Bonus/Commission Income
    if row['bonus_commission_income'] > 10000:
        credit_score += 20
    elif row['bonus_commission_income'] > 5000:
        credit_score += 10
    elif row['bonus_commission_income'] < 5000:
        credit_score += 0

    # Employment Status - Job Stability
    if row['job_stability'] == 'stable':
        credit_score += 30
    elif row['job_stability'] == 'moderate':
        credit_score += 15
    elif row['job_stability'] == 'unstable':
        credit_score += 0

    # Employment Status - Industry Sector
    if row['industry_stability'] == 'stable':
        credit_score += 20
    elif row['industry_stability'] == 'moderate':
        credit_score += 10
    elif row['industry_stability'] == 'unstable':
        credit_score += 0

    # Existing Debts - Outstanding Loans
    if row['outstanding_loans'] < 5000:
        credit_score += 20
    elif row['outstanding_loans'] < 20000:
        credit_score += 10
    elif row['outstanding_loans'] > 20000:
        credit_score -= 20

    # Existing Debts - Credit Card Balances
    if row['credit_card_balances'] < 1000:
        credit_score += 20
    elif row['credit_card_balances'] < 5000:
        credit_score += 10
    elif row['credit_card_balances'] > 5000:
        credit_score -= 20

    # Utility Data - Bills Payment History
    if row['utility_bills_payment_history'] == 'excellent':
        credit_score += 30
    elif row['utility_bills_payment_history'] == 'good':
        credit_score += 20
    elif row['utility_bills_payment_history'] == 'fair':
        credit_score += 10
    elif row['utility_bills_payment_history'] == 'poor':
        credit_score += 0

    return credit_score

# Calculate credit scores for all rows
df['credit_score'] = df.apply(calculate_credit_score, axis=1)

# Preprocess the data
categorical_features = ['payment_history', 'credit_mix', 'job_stability', 'industry_stability', 'utility_bills_payment_history']
numerical_features = ['late_payments', 'bankruptcies', 'credit_utilization', 'outstanding_balances', 'oldest_account_age', 
                      'avg_account_age', 'recent_inquiries', 'employment_income', 'bonus_commission_income', 'outstanding_loans', 
                      'credit_card_balances']

# Encode categorical features
encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(df[categorical_features]).toarray()

# Scale numerical features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[numerical_features])

# Combine encoded and scaled features
X = np.hstack((encoded_features, scaled_features))
y = df['credit_score']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
model = Sequential()
model.add(Dense(128, input_dim=X_train.shape[1], activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate the model
loss = model.evaluate(X_test, y_test)
print(f'Model Loss: {loss}')

# Save the model
model.save('credit_score_model.h5')

# Define the neural expert system function
def neural_expert_system(input_data):
    encoded_input = encoder.transform([[
        input_data['payment_history'],
        input_data['credit_mix'],
        input_data['job_stability'],
        input_data['industry_stability'],
        input_data['utility_bills_payment_history']
    ]]).toarray()
    
    scaled_input = scaler.transform([[
        input_data['late_payments'],
        input_data['bankruptcies'],
        input_data['credit_utilization'],
        input_data['outstanding_balances'],
        input_data['oldest_account_age'],
        input_data['avg_account_age'],
        input_data['recent_inquiries'],
        input_data['employment_income'],
        input_data['bonus_commission_income'],
        input_data['outstanding_loans'],
        input_data['credit_card_balances']
    ]])
    
    combined_input = np.hstack((encoded_input, scaled_input))
    
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

predicted_score = neural_expert_system(input_data)
print(f'Predicted Credit Score: {predicted_score}')
