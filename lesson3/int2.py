import time
def printPM2:
print ("vvedite chislo: ")
y = int(input())
starttime=time.time()
for j in range(2, y+1):
    for i in range(2, y+1):
        if j % i == 0:
            if (j == i):
                print (j)
            else:
                break
print("Time = ", time.time()-starttime)
