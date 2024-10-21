#Creating two lists one with the names of each day and another list that is empty so I can collect user input.
days = ["Sunday","Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday"] 
steps = []

#This For loop allows me to collect the users steps and store them in my steps list using the append function.
# It also allows me to covert the input into an integer which will be helpfull when getting the total and average steps
for day in days:
    s = int(input(f"How many steps did you take on {day}? : "))
    steps.append(s)

print()

#This for loop allows me to use the zip function which allows me to combind both lists "days" & "steps"
for day, s in zip(days,steps):
    print(f"On {day} you walked:{s} Steps")
print()

# Used sum to add all of the list items together
total_steps = sum(steps)
# Took the total steps and divided it by the number of days 
avg_steps = total_steps / len(days)
# Printed out total steps and days using f-string's
print(f"Your total Steps: {total_steps}" )
print(f"Your average Steps Per Day:{avg_steps}")
