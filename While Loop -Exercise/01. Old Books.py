text = input()
counter_books = 0
bookFound = False
book_name = input()
while book_name != "No More Books":
    if book_name == text:
        bookFound = True
        break
    else:
        counter_books += 1
    book_name = input()
if bookFound:
    print(f"You checked {counter_books} books and found it."  )
else:
    print("The book you search is not here!")
    print(f"You checked {counter_books} books.")
