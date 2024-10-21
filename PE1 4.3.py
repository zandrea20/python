def calculate_interest(principal_amount, interest_rate, investment_time):
    calculated_interest = principal_amount * (1 + (interest_rate / 100) * investment_time)
    print(f"The total amount after {investment_time} years for a principal amount of ${principal_amount:,.2f} "
          f"at an interest rate of {interest_rate}% is: ${calculated_interest:,.2f}")

input_principal_amount = float(input("Enter Principal Amount: "))
input_interest_rate = float(input("Please enter the interest rate as a whole number: "))
input_investment_time = float(input("Please enter the investment time in whole years: "))
calculate_interest(input_principal_amount, input_interest_rate, input_investment_time)
