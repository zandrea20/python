num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Demonstrating the use of logical operators

# Using 'and'
print("\nUsing 'and':")
if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
else:
    print("At least one number is not positive.")

# Using 'or'
print("\nUsing 'or':")
if num1 < 0 or num2 < 0:
    print("At least one number is negative.")
else:
    print("Both numbers are non-negative.")

# Using 'not'
print("\nUsing 'not':")
if not (num1 == 0):
    print(f"The first number is not zero: {num1}")
else:
    print("The first number is zero.")

if not (num2 == 0):
    print(f"The second number is not zero: {num2}")
else:
    print("The second number is zero.")