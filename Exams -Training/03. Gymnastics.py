country = input()
device = input()
difficulty = 0
performance = 0
max_score = 20
if country == "Russia":
    if device == "ribbon":
        difficulty = 9.100
        performance = 9.400
        total_score = difficulty + performance
    elif device == "hoop":
        difficulty = 9.300
        performance = 9.800
        total_score = difficulty + performance
    elif device == "rope":
        difficulty = 9.600
        performance = 9.000
        total_score = difficulty + performance
elif country == "Bulgaria":
    if device == "ribbon":
        difficulty = 9.600
        performance = 9.400
        total_score = difficulty + performance
    elif device == "hoop":
        difficulty = 9.550
        performance = 9.750
        total_score = difficulty + performance
    elif device == "rope":
        difficulty = 9.500
        performance = 9.400
        total_score = difficulty + performance
elif country == "Italy":
    if device == "ribbon":
        difficulty = 9.200
        performance = 9.500
        total_score = difficulty + performance
    elif device == "hoop":
        difficulty = 9.450
        performance = 9.350
        total_score = difficulty + performance
    elif device == "rope":
        difficulty = 9.700
        performance = 9.150
        total_score = difficulty + performance
difference = abs(max_score - total_score)
difference_in_percent = difference / max_score * 100
print(f"The team of {country} get {total_score:.3f} on {device}.")
print(f"{difference_in_percent:.2f}%")

