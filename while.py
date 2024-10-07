bottles = 99
while bottles > 0:
    # This is so that bottles and bottle are defined correctly. This is done by assigining bottle and bottles to bottle_name
    if bottles == 1:
        bottle_name = "bottle"
    else:
        bottle_name= "bottles"

    # Using Print functions to display each line in the song
    print(f"{bottles} {bottle_name} of beer on the wall,")
    print(f"{bottles} {bottle_name} of beer.")
    print("Take one down, pass it around, ")

    # Decreasing the bottles by 1
    bottles -= 1

    if bottles == 0:
        print("No more bottles of beer on the wall!")
    else:
        # The use of bottle_word_next checks for the correct use of bottle or bottles
        if bottles == 1:
            bottle_word_next = "bottle"
        else: 
            bottle_word_next = "bottles"
    #This then prints the next line and then starts it on a new line.
    print(f"{bottles} {bottle_word_next} of beer on the wall.\n")
        
