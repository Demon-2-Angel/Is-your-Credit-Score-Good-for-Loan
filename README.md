# Neural Expert System for Credit Card Prediction

## Overview
This project aims to develop a neural expert system to predict credit scores using machine learning algorithms. The system analyzes various features related to credit card usage and financial behavior to determine the creditworthiness of individuals.

## Repository Structure
The repository contains the following files:

- `app.py`: The main application script that runs the web interface for the credit score prediction system.
- `multiapp.py`: A utility script that manages multiple applications within the main web interface.
- `about_us.py`: A script that provides information about the team and project.
- `credit_score_prediction.py`: The core script that contains the machine learning model and logic for credit score prediction.

## Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Demon-2-Angel/Neural-Expert-System-for-Credit-Card-Prediction.git
    cd Neural-Expert-System-for-Credit-Card-Prediction
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To start the application, run the following command:
```bash
streamlit run app.py
