import calendar
import datetime
def main():
    current_year = datetime.datetime.now().year
    while True:
        try:
            birth_month = int(input("Please enter your birth month (1-12): "))
            if 1 <= birth_month <= 12:
                break
            else:
                print("Please enter a valid month between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 12.")   

    print("\nHere is your birth month calendar for the current year", current_year)
    print(calendar.month(current_year, birth_month))
main()