import streamlit as st

def app():
    st.title("FAQs")
    st.header("Frequently Asked Questions")

    st.subheader("1. What is a good credit score?")
    st.write("""
    A good credit score typically ranges from 700 to 749. Scores above 750 are considered excellent and can qualify you for the best loan terms.
    """)

    st.subheader("2. How often should I check my credit score?")
    st.write("""
    It’s recommended to check your credit score at least once a year. Regular monitoring can help you stay on top of your financial health and spot any inaccuracies.
    """)

    st.subheader("3. How can I improve my credit score?")
    st.write("""
    Improving your credit score involves paying bills on time, reducing credit card balances, avoiding new credit inquiries, and maintaining a diverse credit mix.
    """)

    st.subheader("4. How does my employment income affect my credit score?")
    st.write("""
    While employment income itself doesn’t directly affect your credit score, it is considered in loan predictions and creditworthiness assessments, indicating your ability to repay debts.
    """)

    st.subheader("5. What should I do if I find an error in my credit report?")
    st.write("""
    If you find an error in your credit report, you should immediately contact the credit bureau and the creditor involved to dispute the inaccurate information.
    """)

if __name__ == "__main__":
    app()
