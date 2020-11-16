x1=float(input("Введіть x1:"))
y1=float(input("Введіть y1:"))
x2=float(input("Введіть x2:"))
y2=float(input("Введіть y2:"))
x3=float(input("Введіть x3:"))
y3=float(input("Введіть y3:"))
a=((((x2-x1)**2)+((y2-y1)**2))**1/2)
b=((((x3-x2)**2)+((y3-y2)**2))**1/2)
c=((((x3-x1)**2)+((y3-y1)**2))**1/2)
if a==b or b==c or c==b:
    print("рівнобедренний")
else:    
    print("не рівнобедренний")

