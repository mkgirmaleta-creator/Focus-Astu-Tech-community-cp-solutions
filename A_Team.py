n=int(input())
count=0
for i in range(n):
    a=list(map(int, input().split()))
    if sum(a)>=2:
        count+=1
print(count)