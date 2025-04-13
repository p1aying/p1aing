n=int(input())

row=[i for i in range(1,n+1)]
for i in range(n):
    if i%2==0:
        for i in range(n):    
            print(row[i],end="")
        print()
    else:
        row.reverse()
        for i in range(n):    
            print(row[i],end="")
        row.reverse()
        print()