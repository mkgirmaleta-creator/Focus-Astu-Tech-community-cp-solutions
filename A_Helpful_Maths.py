a=sorted(list(map(int, input().split("+"))))
s=""

for i in a:
    s+=str(i)+"+"
    
print(s[:-1])



