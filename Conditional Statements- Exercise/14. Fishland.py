price_of_mackerel = float(input())
price_of_sprat = float(input())
quantity_of_bonito = float(input())
quantity_of_scad = float(input())
quantity_of_mussels = int(input())
price_of_bonito = price_of_mackerel * 1.6
price_of_scad = price_of_sprat * 1.8
price_of_mussels = 7.5
needed_money = price_of_bonito * quantity_of_bonito + price_of_scad * quantity_of_scad + price_of_mussels * quantity_of_mussels
print(f"{needed_money:.2f}")
