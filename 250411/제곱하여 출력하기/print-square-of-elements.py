a=int(input())
b=list(map(int,input().split()))
c=[x**2 for x in b]
for i in range(len(c)):
    print(c[i], end=" ")