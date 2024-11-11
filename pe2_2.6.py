def main():
    flowers = []
    

    confirm = False
    while not confirm:
        user_input = input("Please input names of Flowers (Input 'done' when finished):")

        if user_input.lower() == 'done':
                confirm = True
        else:
            try:
                if not user_input.isalpha():
                    # Found raise exception on W3 schools, was trying to find a way to display error if user inputed a number 
                    raise ValueError("User Input was invalid: Valid inputs must only contain letters.")
                flowers.append(user_input)
                print(f"Added '{user_input}' to the list. ")
            except ValueError as e:
                print(e)

        print("\nYou have finished inputing flower names.")
        print ("Flowers you added")
        for i, flower in enumerate(flowers, start=1):
            print (f"{i} - {flower}")


        search = input ("\n Would you like to search for flowers?(yes/no)").lower()
        if search == 'yes':
            s_term = input("Enter the flower name you would like to search for:").lower()

            if s_term in flowers:
                print(f"{s_term} is in your list.")
            else:
                print (f"{s_term} is not in your list.")
        else: 
            print("Leaving Search.")
main()
