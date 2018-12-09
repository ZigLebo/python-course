from math import *
print("Vvedite vse koefficienti")
a,b,c=list(map(float, input().split()))
discr=b*b-4*a*c
if discr<0:
    print("kornei net")
elif discr==0:
    x=-b/(2*a)
    print("odin koren=", x)
else: #d>0
    x1=(-b+sqrt(discr))/(2*a)
    x2=(-b-sqrt(discr))/(2*a)
    print("1 koren=", x1, ", 2 koren=", x2)
