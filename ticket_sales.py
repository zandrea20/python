# Creating a list with a range of 1-20 for 20 seats
seats= list(range(1,21))
# Showing user avalible seats
print(f"These are the available seats: {seats}")

#Using while statement to execute not only colleting user data and desplaying but to finish the purchase as well.
while True:
    user_seat =int(input("Enter a seat number (1-20), or Please enter 0 to finish your purchase : "))
   #Ends loop if user inputs 0
    if user_seat == 0 :
        break
    # This removes the seat that the user inputed and displays the seats left
    elif user_seat in seats:
        seats.remove(user_seat)
        print(f"Seats {user_seat} has been reserved.")
        print(f"Avaliable seats: {seats}")
    else:
        # Used in case user puts in an invalid input
        print(f"Invalid name, please print a number (1-20) or 0 to complete your purchase")
    

   

        
    