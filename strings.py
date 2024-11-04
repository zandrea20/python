def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    for char in example_string:
        print(f"Iterating through the string:{char}")

    # TODO: Find and print the character with the minimum ASCII value in the string
    min_char =min(example_string)
    print(f"\nCharacter with the minimum ASCII value:{ord(min_char)}")

    # TODO: Find and print the character with the maximum ASCII value in the string
    max_char =max(example_string)
    print(f"\nCharacter with the maximum ASCII value:{ord(max_char)}")

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    index = example_string.index('o')
    print(f"\nIndex of 'o':{index}")

    # TODO: Convert the string into a list of characters and print the list
    char_list = list(example_string)
    print(f"\nConverting string to a list of characters:{char_list}")

    # TODO: Count and print the number of occurrences of 'o' in the string
    
    print(f"\nCount of 'o' in the string: {example_string.count('o')}")


main()
