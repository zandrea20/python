class NotNumericError(Exception):
    def __init__(self, message ="Input is not a valid number"):
        self.message = message
        super().__init__(self.message)

def number_prompt():
    while True:
        try:
            user_input = input("Please enter a number: ")

            if not user_input.isdigit():
                raise NotNumericError("The input is not a numeric value.")
            
            number = int(user_input)

        except NotNumericError as e:
            print(f"Error: {e}")

        else:
            print(f"Sucess, You entered the number: {number}")
            break

        finally:
            print("End of input check. Please try again.")

number_prompt()