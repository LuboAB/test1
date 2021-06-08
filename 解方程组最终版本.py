x1=float(input("x1\n"))
y1=float(input("y1\n"))
x2=float(input("x2\n"))
y2=float(input("y2\n"))
x3=float(input("x3\n"))
y3=float(input("y3\n"))
x4=float(input("x4\n"))
y4=float(input("y4\n"))

k1=(y2-y1)*1.0/(x2-x1)
b1=y1*1.0-x1*k1*1.0
if (x4-x3)==0:
    k2=None
    b2=0
else:
    k2=(y4-y3)*1.0/(x4-x3)
    b2=y3*1.0-x3*k2*1.0
if k2==None:
    x=x3
else:
    x=(b2-b1)*1.0/(k1-k2)
y=k1*x*1.0+b1*1.0
print("交点为")
print(x,y)
