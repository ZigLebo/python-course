print("print number")
n=int(input())
a=[True]*n
print(a)
for i in range(2, len(a)):
        if a[i]:
            print(i, end=" ")
            j=1
            while j*i<=n:
                a[i*j]=False
                j+=1
        print(a)
