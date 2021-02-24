command = input()
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_tickets = 0
while command != "Finish":
    movie_title = command
    free_seats = int(input())
    current_sold_tickets = 0
    while free_seats > current_sold_tickets:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        elif type_of_ticket == "student":
            student_tickets += 1
        elif type_of_ticket == "standard":
            standard_tickets += 1
        elif type_of_ticket == "kid":
            kids_tickets += 1
        current_sold_tickets += 1
        total_tickets += 1
    percent_occupancy_hall = current_sold_tickets / free_seats * 100
    print(f"{movie_title} - {percent_occupancy_hall:.2f}% full.")
    command = input()
percent_student_tickets = student_tickets / total_tickets * 100
percent_standard_tickets = standard_tickets / total_tickets * 100
percent_kids_tickets = kids_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kids_tickets:.2f}% kids tickets.")
