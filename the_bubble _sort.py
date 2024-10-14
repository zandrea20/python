# This allows me to take all 5 names in one input and insert them into a list.
names_list = input("Please Input 5 names seperated by commas:").split(',')

swapped = True

while swapped:
    swapped = False 
    for i in range(len(names_list) - 1):
        # Compare adjacent elements
        if names_list[i] > names_list[i + 1]:
            swapped = True  # A swap is needed
            # Swap the elements
            names_list[i], names_list[i + 1] = names_list[i + 1], names_list[i]

print(names_list)

names_list.reverse()

print(names_list)
