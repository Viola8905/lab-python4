x=float(input("Введіть x:"))
y=float(input("Введіть y:"))
e=2.7
if y==x:
    z=y*x  
elif y<x:
    z=y*e**x
elif y>x:
    z=x*e**y    
else:
    z=none
print("z=",z)
