n,m,a=map(int,input().split())
if(n%a==0):
    d=n//a
else:
    d=(n//a)+1
if(m%a==0):
    k=m//a
else:
    k=(m//a)+1

print(d*k)