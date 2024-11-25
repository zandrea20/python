def main():
    date = input("Please Enter the date(M/D/Y):")
    time = input("Please Enter the time:") 
    entry =input("Enter your Diary entry:")

    file = open("diary.txt", "a")

    file.write(f"Date: {date}\n")
    file.write(f"Time:{time}")
    file.write(f"Diary Entry: {entry}\n")
        
    file.close()

    print("Your diary entry has been saved successfully!")\
    
main()