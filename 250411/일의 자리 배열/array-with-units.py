a=list(map(int,input().split()))

for i in range(10):
    print(a[i], end=" ")
    k=a[i]+a[i+1]
    result=[int(d) for d in str(k)]
    a.append(result[-1])
