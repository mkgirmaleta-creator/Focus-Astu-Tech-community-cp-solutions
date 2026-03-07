s=input()
nupper=0
nlower=0
for char in s:
    if char.isupper():
        nupper+=1
    else:
        nlower+=1
if nupper>nlower:
    print(s.upper())
elif nupper<=nlower:
     print(s.lower())

