import random
from selectionl10 import *
n=int(input("vvedite kolichestvo"))
#A=[]
#for i in range(1,n+1):
#    A.append(i)
#print(A)
A=[i for i in range(1,n+1)]
random.shuffle(A)
print(A)
print(selectionsort(A))
