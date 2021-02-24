number_of_cargo = int(input())
bus_load = 0
truck_load = 0
train_load = 0
for number_of_cargo in range(1, number_of_cargo + 1):
    cargo_load = int(input())
    if cargo_load <= 3:
        bus_load += cargo_load
    elif 4 <= cargo_load <= 11:
        truck_load += cargo_load
    elif cargo_load >= 12:
        train_load += cargo_load
sum_cargo = bus_load + truck_load + train_load
average_sum_for_transport = (bus_load * 200 + truck_load * 175 + train_load * 120) / sum_cargo
bus_percent_load = bus_load / sum_cargo * 100
truck_percent_load = truck_load / sum_cargo * 100
train_percent_load = train_load / sum_cargo * 100
print(f"{average_sum_for_transport:.2f}")
print(f"{bus_percent_load:.2f}%")
print(f"{truck_percent_load:.2f}%")
print(f"{train_percent_load:.2f}%")





