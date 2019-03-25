import sys, math

A = float(input("Enter side A of triangle: "))
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))
t = [A, B, C] #Список сторон треугольника


Big_side = max(t) # Из не равенства треугольника длина
                # наибольшей стороны додлжна быть меньшей
                # либо равной сумме 2х остальных.
t.remove(Big_side)
Sum = sum(t)

if Big_side <= Sum:
    p = eval("1/2*(A+B+C)")
    sq = eval("(p*(p-A)*(p-B)*(p-C))**0.5")  # формула Герона
    print("Perimetr is: " + str(A + B + C))
    print("Square is: " + str(sq))
else:
    print("Не правильный какойто у вас тут триугольник*(")
    sys.exit()
