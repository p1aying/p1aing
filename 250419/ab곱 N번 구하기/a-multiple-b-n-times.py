n=int(input())
sum=1
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        sum*=i
    print(sum)
    sum=1