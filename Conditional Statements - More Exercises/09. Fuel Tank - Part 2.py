type_of_fuel = input()
fuel_quantity = float(input())
possession_club_cart = input()
price_of_gasoline = 2.22
price_of_diesel = 2.33
price_of_gas = 0.93
end_price_gasoline = 0
end_price_diesel = 0
end_price_gas = 0
if possession_club_cart == "Yes":
 price_of_gasoline -= 0.18
 price_of_diesel -= 0.12
 price_of_gas -= 0.08
elif possession_club_cart == "No":
 price_of_gasoline = 2.22
 price_of_diesel = 2.33
 price_of_gas = 0.93
if 20 <= fuel_quantity <= 25:
    end_price_gasoline = fuel_quantity * price_of_gasoline * 0.92
    end_price_diesel = fuel_quantity * price_of_diesel * 0.92
    end_price_gas = fuel_quantity * price_of_gas * 0.92
elif fuel_quantity > 25:
    end_price_gasoline = fuel_quantity * price_of_gasoline * 0.90
    end_price_diesel = fuel_quantity * price_of_diesel * 0.90
    end_price_gas = fuel_quantity * price_of_gas * 0.90
else:
    end_price_gasoline = fuel_quantity * price_of_gasoline
    end_price_diesel = fuel_quantity * price_of_diesel
    end_price_gas = fuel_quantity * price_of_gas
if type_of_fuel == "Gasoline":
    print(f"{end_price_gasoline:.2f} lv.")
elif type_of_fuel == "Diesel":
    print(f"{end_price_diesel:.2f} lv.")
elif type_of_fuel == "Gas":
    print(f"{end_price_gas:.2f} lv.")


