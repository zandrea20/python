# This program is designed to check the users grade 
#This defines each letter grade paramaters and output
def find_letter_grade(letter_grade):
    if 90 <= letter_grade <=100: return 'A'
    elif 80 <= letter_grade < 89: return 'B'
    elif 70 <= letter_grade <79: return 'C'
    elif 60 <= letter_grade <69: return 'D'
    else: return 'F'

try:
    #Asking the user for their grade
    grade_imput = float(input("Please Enter Your Grade (0-100): "))

    # This allows me to check if their imput fits the parameters of 0-100 and prints out the approprite response (The letter grade or Error message)
    if 0 <= grade_imput <= 100:
        letter_grade= find_letter_grade(grade_imput)
        print(f"Your letter grade is: {letter_grade}")
    else:
            print("Error: Please enter a valid number between 0-100.")
except ValueError:
    print("Error: Please Enter a valid grade.")