# This program is aimed to input their total budget and the amount spent in various categories 
# and display what percentage of the total budget each category represents.
budget = float(input("Enter Your Budget: $"))

# Creating a categories variable allows me to make a list of each category and spending amounts.
categories = {
    "Housing (Rent or Mortgage)": 0,
    "Utilities": 0,
    "Groceries": 0,
    "Transportation": 0,
    "Health Care": 0,
    "Personal Care": 0, 
    "Clothing": 0,
    "Debt": 0,
}

# Asking the user for the amount spent for each category and storing it.
for category in categories.keys():  # Using categories.keys() allows access to each category without hardcoding names.
    amount_spent = float(input(f"Please enter the amount spent on {category}: $"))  # Convert input to float.
    categories[category] = amount_spent 

# Display the Budget Breakdown
print("\nBudget Breakdown")
print(f"{'Category':<30}{'Amount Spent ($)':<20}{'Percentage Of Budget (%)':<30}")  # Corrected header
print("-" * 100)

# This for loop calculates and displays the % spent of the budget
for category, amount in categories.items():
    percentage = (amount / budget) * 100  # Calculate the percentage of the total budget
    print(f"{category:<30}${amount:<20}{percentage:.2f}%")  # Correctly format the output
