YEAR = int(input("Год для проверки на высокосность: "))
print(YEAR%400)
print(YEAR%100)
print(YEAR%4)

if YEAR % 400 != 0 and YEAR % 100 == 0:
    print("Год НЕ высокосный")
elif YEAR % 4 == 0 or YEAR % 400 == 0:
    print("Год высокосный")
else:
    print("Год НЕ высокосный")