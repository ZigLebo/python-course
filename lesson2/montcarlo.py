import random
random.seed(42)
s_sq=16
n=1000000
n_p=0
for i in range(n):
        x=random.uniform(0,4)
        y=random.uniform(0,4)
        if y<=-(x-2)*(x-2)+4:
            n_p+=1
print("ploshad = {}".format((s_sq*n_p)/n))
