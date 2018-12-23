print("Print 3 sides of a triangle")
from math import *
a,b,c=list(map(float, input().split()))
p=(a+b+c)/2
S=sqrt(p*(p-a)*(p-b)*(p-c))
print("Area of triangle ", S)
