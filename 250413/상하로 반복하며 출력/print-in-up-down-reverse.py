N=int(input())

exm=[i for i in range(1,N+1)]
j=0
flag=0
matrix=[]
#print(exm)
for i in range(N):
    for _ in range(N):
        if flag==0:
            print(exm[j],end="")
            flag=1
        else:
            if flag==1:
                print(exm[-(j+1)],end="")
                flag=0
    j+=1
    flag=0
    print()
