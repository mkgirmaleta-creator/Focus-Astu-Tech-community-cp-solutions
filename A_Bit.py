n=int(input())
c=0
for i in range(n):
    a=list(input()
           )
    if "+" in a:
        c+=1
    else:
        c-=1
print(c)