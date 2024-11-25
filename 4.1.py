def two_letter_combinations(char_list):
    for first_char in char_list:
        for second_char in char_list:
            yield first_char + second_char

def main():
    char_list = ['v','w','x','y','z']

    for combination in two_letter_combinations(char_list):
        print(combination)
main()