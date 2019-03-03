def is_a_book(ISBN):
    ISBN=ISBN.replace("-","")
    digits=list(map(int,ISBN[:-1]))
    koef=list(range(len(digits)+1,1,-1))
    print(digits, koef, sep="\n")
    s=0
    for i in range(len(digits)):
        j=digits[i]*koef[i]
        s+=j
    res=(s+int(ISBN[-1]))%11
    print(11-s%11)
    print(res,s)
    if res==0:
        return True
    else:
        return False

if __name__=="__main__":
    ISBN=input()
    print(is_a_book(ISBN))
