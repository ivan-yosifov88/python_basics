number_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
total_time = number_pages / pages_per_hour
hours_to_read = total_time / number_of_days
print(hours_to_read)