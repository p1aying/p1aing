a=int(input())
b=list(map(int,input().split()))
c=[]
for x in b:
    if x%2==0:
        c.append(x)
    else:
        continue

c.reverse()
for i in range(len(c)):
    print(c[i], end=" ")