a,b=map(int,input().split())
c=a
print(a,end=" ")
while(1):
    if c%2==0:
        c+=3
        if c<=b:
            print(c,end =" ")
        else:
            break
    else:
        c*=2
        if c<=b:
            print(c,end =" ")
        else:
            break
        
