def mortgage_calulator(principal, apr, term):
    '''
    Calculates the monthly payment for a loan
    Inputs:
    - total amount of the loan
    - annual percentage rate of the loan
    - the duration of the loan in months

    Output:
    - formatted monthly payment (example: $452.86)
    '''
    monthly_interest_rate = (apr / 12) / 100

    denominator = (1 - (1 + monthly_interest_rate) ** (-term))
    monthly_payment = principal * (monthly_interest_rate / denominator)

    return monthly_payment

while True:
    # take input
    loan_amount = int(input("What is your total loan amount? "))
    annual_percentage_rate = int(input("What is the APR? "))
    loan_duration = int(input("What is the duration of the loan (in months)? "))

    loan_result = mortgage_calulator(loan_amount, annual_percentage_rate, loan_duration)
    print()
    print(f"${loan_result:.2f}")
    print()

    answer = input("Would you like to calculate another loan? (y/n) ")
    print()

    if answer == 'n':
        break
