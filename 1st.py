import sys, math

A = float(input("Enter side A of triangle: "))
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))
t = [A, B, C] #Список сторон треугольника

for i in t:
    if i<0:
        print("Значение не может быть отрицательным")
        sys.exit()


Big_side = max(t) # Из не равенства треугольника длина
                # наибольшей стороны додлжна быть меньшей
                # либо равной сумме 2х остальных.
t.remove(Big_side)

Sum1 = math.fabs(t[0])
Sum2 = math.fabs(t[1])
SUM = Sum1 + Sum2

if math.fabs(Big_side) <= SUM:
    p = eval("1/2*(A+B+C)")
    sq = eval("(p*(p-A)*(p-B)*(p-C))**0.5")  # формула Герона
    print("Perimetr is: " + str(A + B + C))
    print("Square is: " + str(sq))
else:
    print("Не правильный какойто у вас тут триугольник*(")
    sys.exit()
