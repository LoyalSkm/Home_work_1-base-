val = float(input("Enter number: "))
if val%6 == 0:
    num = val**3
else:
    num = eval("(val-5)*2")
print("number is: " + str(num))