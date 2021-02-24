number_of_groups = int(input())
total_tourists = 0
trekking_group_Musala = 0
trekking_group_Mont_blanc = 0
trekking_group_Kilimanjaro = 0
trekking_group_K2 = 0
trekking_group_Everest = 0
for groups in range(number_of_groups):
    number_of_tourists = int(input())
    if number_of_tourists <= 5:
        trekking_group_Musala += number_of_tourists
    elif 6 <= number_of_tourists <= 12:
        trekking_group_Mont_blanc += number_of_tourists
    elif 13 <= number_of_tourists <= 25:
        trekking_group_Kilimanjaro += number_of_tourists
    elif 26 <= number_of_tourists <= 40:
        trekking_group_K2 += number_of_tourists
    elif number_of_tourists >= 41:
        trekking_group_Everest += number_of_tourists
    total_tourists += number_of_tourists
percent_trekking_group_Musala = trekking_group_Musala / total_tourists * 100
percent_trekking_group_Mont_blanc = trekking_group_Mont_blanc / total_tourists * 100
percent_trekking_group_Kilimanjaro = trekking_group_Kilimanjaro / total_tourists * 100
percent_trekking_group_K2 = trekking_group_K2 / total_tourists * 100
percent_trekking_group_Everest = trekking_group_Everest / total_tourists * 100
print(f"{percent_trekking_group_Musala:.2f}%")
print(f"{percent_trekking_group_Mont_blanc:.2f}%")
print(f"{percent_trekking_group_Kilimanjaro:.2f}%")
print(f"{percent_trekking_group_K2:.2f}%")
print(f"{percent_trekking_group_Everest:.2f}%")



