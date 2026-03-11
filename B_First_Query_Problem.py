n=int(input())
a=list(map(int, input().split()))
q=int(input())
for i in range(q):
    queries=list(map(int, input().split()))
    if queries[0]==1:
        a[int(queries[1])-1]=queries[-1]
    else:
        print(a[int(queries[-1])-1])
       
