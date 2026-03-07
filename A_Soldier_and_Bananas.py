k,n,w=map(int, input().split())
tprice=0
for i in range(1,w+1):
    tprice+=+k*i
if tprice>n:
    print(tprice-n)
else:
    print(0)