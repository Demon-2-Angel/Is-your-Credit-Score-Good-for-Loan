import streamlit as st
from multiapp import MultiApp
from pages import credit_history_theory, credit_score_prediction, about_us, FAQs

app = MultiApp()

# Add all your application here
app.add_app("Credit History Theory", credit_history_theory.app)
app.add_app("Credit Score Prediction", credit_score_prediction.app)
app.add_app("About Us", about_us.app)
app.add_app("FAQs", FAQs.app)

# Run the main app
app.run()
