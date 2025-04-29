from collections import deque
n = int(input())
A = list(map(int, input().split()))
dist=deque()
for i in range(n-1,-1,-1):
    dist.append((i))
a=[0 for _ in range(n)]
kk=0
sum=0
for i in range(1,n+1):
    for j in range(n):
        k=dist.popleft()
        sum+=A[j]*k
        dist.append(k)
        #print(f"{A[j]*k}")
    a[kk]=sum
    sum=0
    dist.popleft()
    dist.append(i)
    kk+=1
print(min(a))