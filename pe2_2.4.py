def main():
    books = []
    while len(books) < 10:
        books = input("Please enter a book title:")
        formatted_book = books.title()
        books.append(formatted_book)
    sorted_books = sorted(books)

    print("\nBook titles in in alphabetical order:")
    for title in sorted_books:
        print(title)
main()