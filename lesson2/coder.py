print("Vvedite stroky")
s=input()
print("Vvedite Smechenie")
d=int(input())
i=0
out=""
while i<len(s):
  if s[i]==" ":
    out+=" "
  else:
    out+=chr(97+((ord(s[i])-97)+d)%26)
  i+=1
print(out)
