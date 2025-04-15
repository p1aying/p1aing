a,b=map(int,input().split())

sum1=1
for i in range(1,b+1):
    if i%a==0:
        sum1*=i
print(sum1)