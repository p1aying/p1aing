a,b,c=map(int,input().split())

if a>=b:
    if a>=c:
        print(a)
    else:
        print(c)
elif b>=a:
    if b>=c:
        print(b)
    else:
        print(c)
elif c>=a:
    if c>=b:
        print(c)
    else:
        print(b)