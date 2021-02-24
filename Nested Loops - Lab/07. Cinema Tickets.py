total_sold_tickets = 0
number_of_student_tickets = 0
number_of_standard_tickets = 0
number_of_kid_tickets = 0
command = input()
while command != "Finish":
    movie_name = command
    free_seats = int(input())
    sold_tickets_for_current_film = 0
    percent_occupy_hall = 0
    while free_seats > sold_tickets_for_current_film:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        elif type_of_ticket == "student":
            number_of_student_tickets += 1
        elif type_of_ticket == "standard":
            number_of_standard_tickets += 1
        elif type_of_ticket == "kid":
            number_of_kid_tickets += 1
        sold_tickets_for_current_film += 1
        total_sold_tickets += 1
        percent_occupy_hall = sold_tickets_for_current_film / free_seats * 100
    print(f"{movie_name} - {percent_occupy_hall:.2f}% full.")
    command = input()
percent_student_tickets = number_of_student_tickets / total_sold_tickets * 100
percent_standard_tickets = number_of_standard_tickets / total_sold_tickets * 100
percent_kid_tickets = number_of_kid_tickets / total_sold_tickets * 100
print(f"Total tickets: {total_sold_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")

