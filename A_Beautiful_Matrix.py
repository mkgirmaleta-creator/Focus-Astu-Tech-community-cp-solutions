m=[]
for i in range(5):
    a=list(map(int, input().split()))
    m.append(a)

k,l=0,0
for i in range(5):
    for j in range(5):
        if m[i][j]==1:
            k=i
            l=j

print(abs(2-k) + abs(2-l))
