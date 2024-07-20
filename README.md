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
This will start the web application on a local server. Open your web browser and navigate to the provided URL to interact with the credit score prediction system.

## Application Modules
### `app.py`
This script initializes and runs the Streamlit web application, integrating various modules to provide a user-friendly interface for credit score prediction.

### `multiapp.py`
This script provides functionality to manage multiple applications within the main Streamlit interface. It allows for the seamless integration of different components of the project.

### `about_us.py`
This script displays information about the project team and the objectives of the credit score prediction system. It serves as an informational page within the web application.

### `credit_score_prediction.py`
This script contains the machine learning model and prediction logic. It processes user input, applies the trained model, and returns a predicted credit score.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please contact [foraniruddhakumar@gmail.com].


Feel free to replace `[foraniruddhakumar@gmail.com]` with your actual contact email or other relevant contact information.


3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To start the application, run the following command:
```bash
streamlit run app.py
