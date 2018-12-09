alph=[]
n=97
d=2
while n<=122:
    alph+=[n]
    n+=1
new_alph=[]
i=0
while i<len(alph):
    new_alph+=[alph[(i+d)%26]]
    i+=1
