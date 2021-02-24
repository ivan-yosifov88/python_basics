last_sector = input()
sector_a_rows = int(input())
number_of_odd_seats = int(input())
total_seats = 0
for sectors in range(65, ord(last_sector) + 1):
    if sectors > 65:
        sector_a_rows += 1
    even_seats = 0
    for rows in range(1, sector_a_rows + 1):
        if rows % 2 == 0:
            even_seats += 2
        for seats in range(97, (97 + number_of_odd_seats) + even_seats ):
            even_seats = 0
            total_seats += 1
            print(f"{chr(sectors)}{rows}{chr(seats)}")
print(total_seats)
