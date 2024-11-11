def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    try:
        for index, item in enumerate(top_artists, start=1):
            print(f"{index}. {item}")

        replace_input = int(input("Which place would you like to replace (1-10): "))
        # To make the code more user friendly insted of asking for the index position I asked for the list position.
        # I still added Index Error as the assignment ask for but this should prevent the user from triggering said error. 
        if 1 <= replace_input <= len(top_artists):
            replace_index = replace_input -1

            new_artist = input(f"Enter the artist you would like to add '{top_artists[replace_index]}':")

            top_artists[replace_index] = new_artist

            print("\n Updated Top artists")
            for i, item in enumerate(top_artists, start=1):
                print(f"{i}. {item}")

    except (ValueError, IndexError) as e:
        print(f"An error as occured: {e}")


      

main()
    