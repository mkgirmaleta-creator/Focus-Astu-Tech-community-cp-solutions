digits =[4,3,2,10]
st=""
for  i in digits:
    st+=str(i)
rt=[]
l=int(st)+1
rt.extend(map(int, str(l)))
print(rt)
 
