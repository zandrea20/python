def main():
    try:
        with open("sales_totals.txt", "r") as file:
            total = 0
            count = 0

            for line in file:
                stripped_line = line.strip()
                
                try:
                    number = float(stripped_line)
                    total += number 
                    count += 1

                    print(f"Number: {number:.2f}")
                except ValueError:
                    print(f"Alert: Could not convert '{stripped_line}' to a number.")

                if count > 0:
                    average = total / count
                    print(f"\nTotal: {total:.2f}")
                    print(f"Count: {count}")
                print(f"Average: {average:.2f}")
            else:
                print("\nNo valid numbers found in the file.")

    except FileNotFoundError:
        print("Error: The file 'sales_totals.txt' was not found.")
    except IOError:
        print("Error: An error occurred while reading the file.")
main()