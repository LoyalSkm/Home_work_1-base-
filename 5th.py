YEAR = ["Обезьяна", "Петух", "Собака",
        "Свинья", "Крыса", "Бык",
        "Тигр", "Кролик","Дакон",
        "Змея", "Лошадь", "Овца"
        ]              # В списке значения от тех что кратны 0
                       # до тех что кратны 11
COLOR = ["(Белый)Металическ", "(Синий)Водян", "(Зеленый)Деревянн", "(Красный)Огненн", "(Желтый)Землян"]
push = (int(input("Какго года будишь?: ")))

calc_col = (int(push % 10))
calc_year = (int(push % 12))


if calc_col in (0, 1): a = 0
if calc_col in(2, 3): a = 1
if calc_col in(4, 5): a = 2
if calc_col in(6, 7): a = 3
if calc_col in(8, 9): a = 4
if calc_year in (0, 2, 3, 4, 9, 10, 11): b = "ая"
elif calc_year in (1, 5, 6) and a == 1: b = "ой"
else: b = "ый"

print("Ты " + str(COLOR[a]) + b + " " + str(YEAR[calc_year]))