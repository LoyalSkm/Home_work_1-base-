A = float(input("Enter side A of triangle: "))
B = float(input("Enter side B: "))
C = float(input("Enter side C: "))
p = eval("1/2*(A+B+C)")                  # разность полупериметра
sq = eval("(p*(p-A)*(p-B)*(p-C))**0.5")  # формула Герона
print("Perimetr is: " + str(A+B+C))
print("Square is: " + str(sq))

