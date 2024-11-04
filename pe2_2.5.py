def main():
    valid = False
    while not valid:
        valid = True
        try:
            password = input("Please input a password that:\n"
                     "- Is between 8 to 20 characters long.\n"
                     "- Contains at least one uppercase letter.\n"
                     "- Contains at least one lowercase letter.\n"
                     "- Includes at least one number.\n"
                     "- Includes at least one symbol from the set: !@#$%&*:\n")
            length = len(password)
            if 8 <= length <= 20:
                print("Password meets length requirements.")
            
            elif len < 8:
                print("This Password is too short.")
                valid = False
            elif len >= 20:
                print("This Password is too long.")
                valid = False
            if any(char.isupper() for char in password):
                print("Password meets uppercase requirements.")
            else:
                print("Password does not contain an uppercase letter.")
                valid = False
            if any(char.islower() for char in password):
                print("Password meets lowercase requirements.")
            
            else:
                print("Password entered does not contain a lower case letter")
            has_symbol = False
            symbol = ['!','@','#','$','%','*']
            for s in symbol:
                for c in password:
                    if s == c:
                        has_symbol = True
            if has_symbol == False:
                print("You need to include a symbol")
                valid = False
            if valid:
                confirmation = input("Please re-enter you password for confirmation:")
                if password  == confirmation:
                    print("Your password is vaild!")
                    break
            else:
                print("Password does not match please try again.")
        except ValueError:
            print("There was a value error. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

main()
