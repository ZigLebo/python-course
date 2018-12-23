print("print juice volume")
v=int(input())
print("print juice price")
p=int(input())
print("print stock juice volume")
vs=int(input())
print("print stock juice price")
ps=int(input())
j=p/v
sj=ps/vs
if j>sj:
    print("stock juice is more profitable")
else:
    print("juice is more profitable")
