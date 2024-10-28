# Simple Python program to calculate the square of a number

def square_number():
    number = input("Enter a number to square: ")
    try:
        number = int(number)
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    if number >= 0 :
         squared_number = int(number) ** 2
         print(f"The square of {number} is {squared_number}.")
    else:
         print("Please input a non negative number")

square_number()
    