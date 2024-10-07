#This program is designed to Ask the user for their age. Check to see if the user is old enough to drive, vote, legally buy alcohol,eligible for a senior discount 
#Creating age limits for each requirment
driving_age= 16
drinking_age= 21
voting_age= 18
senior_age=60

# Asking for the Users age
age = int(input("Please enter Your age: "))

if age >= driving_age:
    print("You are eligible to drive a car. ")
else:
    print("You are not eligible to drive a car")


if age >= drinking_age:
    print("You are eligible to buy alcohol. ")
else:
    print("You are not eligible to buy alcohol")

if age >= voting_age:
    print("You are eligible to vote in the USA. ")
else:
    print("You are not eligible to vote in the USA")


if age >= senior_age:
    print("You are eligible for a senior discount. ")
else:
    print("You are not eligible for a senior discount")


