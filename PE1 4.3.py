def calculate_interest(interest_rate, principal_amount, investment_time):
    calculated_interest = (principal_amount*investment_time*interest_rate) / 100
    return calculated_interest

principal_amount = float(input("Please input your principal amount:"))
interest_rate = float(input("Please input your intrest rate as a whole number (5% would be 5):"))
investment_time = float(input("Please input your time invested in whole years:"))

calculated_interest = calculate_interest(principal_amount, interest_rate, investment_time)

print(f"The simple interest for a principal amount of ${principal_amount:,.2f} "
      f"at an interest rate of {interest_rate}% over a period of "
      f"{investment_time} years is: ${calculated_interest:,.2f}")
