def calculate_credit_score():
    # Introductory statement
    print("Welcome to the Credit Score Calculator!")
    print("Please provide the following information to calculate your credit score.")
    print("For each category, you will be given specific options to choose from. Enter the option that best describes your situation.")
    print("Let's get started!\n")

    credit_score = 0
    
    # Credit History - On-Time Payments
    print("Credit History - On-Time Payments:")
    print("Your credit history is an important factor in determining your credit score. It includes your payment history for credit accounts.")
    print("Please select the option that best describes your payment history for on-time payments.")
    payment_history_options = ['excellent', 'good', 'fair', 'poor']
    print(f"Options: {', '.join(payment_history_options)}")
    payment_history = input("Enter payment history: ").strip().lower()
    if payment_history == 'excellent':
        credit_score += 100
    elif payment_history == 'good':
        credit_score += 80
    elif payment_history == 'fair':
        credit_score += 50
    elif payment_history == 'poor':
        credit_score += 20
    
    # Credit History - Late Payments
    print("\nCredit History - Late Payments:")
    print("Late payments can negatively impact your credit score. Enter the total number of late payments you have had.")
    late_payments = int(input("Enter the number of late payments: ").strip())
    if late_payments == 0:
        credit_score += 30
    elif 1 <= late_payments <= 2:
        credit_score += 20
    elif 3 <= late_payments <= 4:
        credit_score += 10
    elif late_payments > 4:
        credit_score -= 20
    
    # Credit History - Defaults and Bankruptcies
    print("\nCredit History - Defaults and Bankruptcies:")
    print("Defaults and bankruptcies are severe negative marks on your credit history. Enter the total number of bankruptcies you have had.")
    bankruptcies = int(input("Enter the number of bankruptcies: ").strip())
    if bankruptcies == 0:
        credit_score += 50
    elif bankruptcies == 1:
        credit_score -= 50
    elif bankruptcies > 1:
        credit_score -= 100
    
    # Amounts Owed - Credit Utilization Ratio
    print("\nAmounts Owed - Credit Utilization Ratio:")
    print("The credit utilization ratio is the amount of credit you are using compared to your total available credit. Enter the ratio as a percentage.")
    credit_utilization = float(input("Enter credit utilization ratio (as a percentage): ").strip())
    if credit_utilization < 10:
        credit_score += 50
    elif credit_utilization < 30:
        credit_score += 30
    elif credit_utilization < 50:
        credit_score += 10
    elif credit_utilization > 50:
        credit_score -= 30
    
    # Amounts Owed - Outstanding Balances
    print("\nAmounts Owed - Outstanding Balances:")
    print("Outstanding balances refer to the total amount of money you owe across all credit accounts.")
    outstanding_balances = float(input("Enter outstanding balances: ").strip())
    if outstanding_balances < 1000:
        credit_score += 20
    elif outstanding_balances < 5000:
        credit_score += 10
    elif outstanding_balances > 5000:
        credit_score -= 20
    
    # Length of Credit History - Age of Oldest Account
    print("\nLength of Credit History - Age of Oldest Account:")
    print("The age of your oldest credit account reflects how long you have been managing credit. Enter the age of your oldest account in years.")
    oldest_account_age = float(input("Enter the age of the oldest account (in years): ").strip())
    if oldest_account_age > 10:
        credit_score += 40
    elif oldest_account_age > 5:
        credit_score += 20
    elif oldest_account_age < 3:
        credit_score += 10
    
    # Length of Credit History - Average Age of Accounts
    print("\nLength of Credit History - Average Age of Accounts:")
    print("The average age of your credit accounts helps determine your experience with managing credit. Enter the average age of your accounts in years.")
    avg_account_age = float(input("Enter the average age of accounts (in years): ").strip())
    if avg_account_age > 7:
        credit_score += 30
    elif avg_account_age > 5:
        credit_score += 20
    elif avg_account_age < 3:
        credit_score += 10
    
    # Credit Mix - Types of Credit Accounts
    print("\nCredit Mix - Types of Credit Accounts:")
    print("A diverse mix of credit accounts (e.g., credit cards, mortgages, auto loans) can positively affect your credit score. Select the option that best describes your credit mix.")
    credit_mix_options = ['diverse', 'moderate', 'limited']
    print(f"Options: {', '.join(credit_mix_options)}")
    credit_mix = input("Enter credit mix: ").strip().lower()
    if credit_mix == 'diverse':
        credit_score += 20
    elif credit_mix == 'moderate':
        credit_score += 10
    elif credit_mix == 'limited':
        credit_score += 0
    
    # New Credit - Recent Credit Inquiries
    print("\nNew Credit - Recent Credit Inquiries:")
    print("Recent credit inquiries indicate that you are actively seeking new credit. Enter the number of recent credit inquiries.")
    recent_inquiries = int(input("Enter the number of recent credit inquiries: ").strip())
    if recent_inquiries == 0:
        credit_score += 20
    elif recent_inquiries <= 2:
        credit_score += 10
    elif recent_inquiries > 2:
        credit_score -= 10
    
    # Income Levels - Employment Income
    print("\nIncome Levels - Employment Income:")
    print("Your employment income affects your ability to repay debts. Enter your total employment income.")
    employment_income = float(input("Enter employment income: ").strip())
    if employment_income > 100000:
        credit_score += 50
    elif employment_income > 50000:
        credit_score += 30
    elif employment_income < 50000:
        credit_score += 10
    
    # Income Levels - Bonus/Commission Income
    print("\nIncome Levels - Bonus/Commission Income:")
    print("Bonus and commission income can supplement your regular income. Enter your total bonus/commission income.")
    bonus_commission_income = float(input("Enter bonus/commission income: ").strip())
    if bonus_commission_income > 10000:
        credit_score += 20
    elif bonus_commission_income > 5000:
        credit_score += 10
    elif bonus_commission_income < 5000:
        credit_score += 0
    
    # Employment Status - Job Stability
    print("\nEmployment Status - Job Stability:")
    print("Job stability indicates the security of your employment. Select the option that best describes your job stability.")
    job_stability_options = ['stable', 'moderate', 'unstable']
    print(f"Options: {', '.join(job_stability_options)}")
    job_stability = input("Enter job stability: ").strip().lower()
    if job_stability == 'stable':
        credit_score += 30
    elif job_stability == 'moderate':
        credit_score += 15
    elif job_stability == 'unstable':
        credit_score += 0
    
    # Employment Status - Industry Sector
    print("\nEmployment Status - Industry Sector:")
    print("The stability of your industry can affect your job security. Select the option that best describes your industry stability.")
    industry_stability_options = ['stable', 'moderate', 'unstable']
    print(f"Options: {', '.join(industry_stability_options)}")
    industry_stability = input("Enter industry stability: ").strip().lower()
    if industry_stability == 'stable':
        credit_score += 20
    elif industry_stability == 'moderate':
        credit_score += 10
    elif industry_stability == 'unstable':
        credit_score += 0
    
    # Existing Debts - Outstanding Loans
    print("\nExisting Debts - Outstanding Loans:")
    print("Outstanding loans refer to the total amount of money you owe on loans. Enter the total amount of your outstanding loans.")
    outstanding_loans = float(input("Enter the amount of outstanding loans: ").strip())
    if outstanding_loans < 5000:
        credit_score += 20
    elif outstanding_loans < 20000:
        credit_score += 10
    elif outstanding_loans > 20000:
        credit_score -= 20
    
    # Existing Debts - Credit Card Balances
    print("\nExisting Debts - Credit Card Balances:")
    print("Credit card balances refer to the total amount of money you owe on credit cards. Enter the total amount of your credit card balances.")
    credit_card_balances = float(input("Enter credit card balances: ").strip())
    if credit_card_balances < 1000:
        credit_score += 20
    elif credit_card_balances < 5000:
        credit_score += 10
    elif credit_card_balances > 5000:
        credit_score -= 20
    
    # Utility Data - Bills Payment History
    print("\nUtility Data - Bills Payment History:")
    print("Your history of paying utility bills on time can impact your credit score.")
    print("Please select the option that best describes your utility bills payment history.")
    utility_bills_payment_history_options = ['excellent', 'good', 'fair', 'poor']
    print(f"Options: {', '.join(utility_bills_payment_history_options)}")
    utility_bills_payment_history = input("Enter utility bills payment history: ").strip().lower()
    if utility_bills_payment_history == 'excellent':
        credit_score += 30
    elif utility_bills_payment_history == 'good':
        credit_score += 20
    elif utility_bills_payment_history == 'fair':
        credit_score += 10
    elif utility_bills_payment_history == 'poor':
        credit_score += 0
    
    return credit_score

# Calculate the credit score
credit_score = calculate_credit_score()
print("Calculated Credit Score:", credit_score)
