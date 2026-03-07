s=input()
ans=""
l=["A","O","Y","E","U","I"]
for char in s:
    if char.upper() not in l:
        ans+="."+char
print(ans.lower())

