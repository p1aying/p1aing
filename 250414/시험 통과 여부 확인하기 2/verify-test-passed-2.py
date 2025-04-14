n=int(input())

pass_count=0
for i in range(n):
    a,b,c,d=map(int,input().split())
    avg=(a+b+c+d)/4
    if avg>=60:
        pass_count+=1
        print("pass")
    else:
        print("fail")
print(pass_count)