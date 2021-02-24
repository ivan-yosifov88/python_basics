from math import ceil
vineyard_area = int(input())
grape_for_one_square_meter = float(input())
needed_wine = int(input())
number_of_workers = int(input())
part_from_vineyard_for_wine = vineyard_area * 0.4
produced_wine = part_from_vineyard_for_wine * grape_for_one_square_meter / 2.5
difference = abs(produced_wine - needed_wine)
wine_for_one_worker = difference / number_of_workers
if produced_wine < needed_wine:
    print(f"It will be a tough winter! More {int(difference)} liters wine needed.")
elif produced_wine >= needed_wine:
    print(f"Good harvest this year! Total wine: {int(produced_wine)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(wine_for_one_worker)} liters per person.")