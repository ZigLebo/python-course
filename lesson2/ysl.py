while True:
    print("Vvedite chislo")
    a=input()
    if a=="stop":
        break
    else:
        if int(a)%2==0:
            print("{0}chetnoe chislo".format(a))
        else:
            print("{0}nechetnoe chislo".format(a))
