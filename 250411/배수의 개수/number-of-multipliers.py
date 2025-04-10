a=[]
b=[]
for i in range(10):
    c=int(input())
    if c%3==0:
        a.append(c)
    if c%5==0:
        b.append(c)
print(len(a),end=" ")
print(len(b))