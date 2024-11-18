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
                if length < 8:
                    print("This Password is too short.")
                    valid = False
                elif length > 20:
                    print("This Password is too long.")
                    valid = False
                else:
                    print("Password meets length requirements.")

                if not any(char.isupper() for char in password):
                    print("Password does not contain an uppercase letter.")
                    valid = False
                else:
                    print("Password meets uppercase requirements.")


                if not any(char.islower() for char in password):
                    print("Password does not contain a lowercase letter.")
                    valid = False
                else:
                    print("Password meets lowercase requirements.")
                symbols = ['!', '@', '#', '$', '%', '&', '*']  
                has_symbol = False  
                for s in symbols:
                    for c in password:
                        if s == c:
                            has_symbol = True
                if has_symbol == False:
                    print("You need to include a symbol (!,@,#,$,%,&,*).")
                    valid = False

                if valid:
                    confirmation = input("Please re-enter you password for confirmation:")
                    if password  == confirmation:
                        print("Your password is vaild!")
                        break
                else:
                    print("Password does not match please try again.")
                    valid = False
            except ValueError:
                print("There was a value error. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

main()
