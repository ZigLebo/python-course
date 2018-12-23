import time
def printPM(n, printres=True):
        starttime=time.time()
        a=[True]*(n+1)
        for i in range(2, len(a)):
            if a[i]:
                if printres:
                    print(i, end=" ")

                j=1
            while j*i<=n:
                a[i*j]=False
                j+=1
        return time.time()-starttime
def printPM2(y, printres=True):
    starttime=time.time()
    for j in range(2, y+1):
        for i in range(2, y+1):
            if j % i == 0:
                if (j == i):
                    if printres:
                        print (j)
                else:
                    break
    return time.time()-starttime
