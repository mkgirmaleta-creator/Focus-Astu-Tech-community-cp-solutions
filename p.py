a=list(map(int, input().split()))
d={}
s=0

for i in a:
    d[i]=d.get(i, 0) + 1

for i in d:
    s+=d[i]//2

print(s)