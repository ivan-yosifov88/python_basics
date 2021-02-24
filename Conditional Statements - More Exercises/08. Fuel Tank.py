type_of_fuel = input()
litres_of_fuel = int(input())
if type_of_fuel == "Diesel":
    if litres_of_fuel >= 25:
        print("You have enough diesel.")
    else:
        print("Fill your tank with diesel!")
elif type_of_fuel == "Gasoline":
    if litres_of_fuel >= 25:
        print("You have enough gasoline.")
    else:
        print("Fill your tank with gasoline!")
elif type_of_fuel == "Gas":
    if litres_of_fuel >= 25:
        print("You have enough gas.")
    else:
        print("Fill your tank with gas!")
else:
    print("Invalid fuel!")

