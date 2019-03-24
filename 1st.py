import sys
A = float(input("Enter side A of triangle: "))
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))
if (A == 0) or (B == 0) or (C == 0):
    print("Не правильный какойто у вас тут триугольник*(")
    sys.exit()
p = eval("1/2*(A+B+C)")                  # разность полупериметра
sq = eval("(p*(p-A)*(p-B)*(p-C))**0.5")  # формула Герона
print("Perimetr is: " + str(A+B+C))
print("Square is: " + str(sq))

