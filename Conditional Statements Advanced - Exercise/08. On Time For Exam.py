hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())
message = ""
time_of_exam = hour_exam * 60 + minute_exam
time_of_arrival = hour_arrival * 60 + minute_arrival
total_time = abs(time_of_exam - time_of_arrival)
if time_of_exam - time_of_arrival > 30:
    message = "Early"
    if total_time > 59:
        hours = total_time // 60
        minutes = total_time % 60
        print(message)
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
    else:
        print(message)
        print(f"{total_time} minutes before the start")
elif 0 <= time_of_exam - time_of_arrival <= 30:
    message = "On time"
    print(message)
    print(f"{total_time} minutes before the start")
elif 0 < time_of_arrival - time_of_exam:
    message = "Late"
    if total_time > 59:
        hours = total_time // 60
        minutes = total_time % 60
        print(message)
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
    else:
        print(message)
        print(f"{total_time} minutes after the start")
