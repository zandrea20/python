
from datetime import datetime

def main():
   
    print("\n\n")
    try:
        today = datetime.today()
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        

        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        delta = today - birthday
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.25
       
        remaining_days = delta.days % 365

        delta_months = remaining_days // 30
        remaining_days %= 30

        delta_weeks = remaining_days // 7
        remaining_days %= 7

        delta_hours = delta.days * 24 + today.hour

        delta_minutes = delta_hours * 60 + today.minute

    
        print(f"You are {int(delta_years)}  years, {delta_months} months, {delta_weeks} weeks, and {remaining_days} days old.")
        print(f"This is also equivalent to: {delta_hours} hours or {delta_minutes} minutes.")


    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()