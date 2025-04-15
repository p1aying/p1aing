mylist=list(map(int,input().split()))

mysum=0
mysum2=0
count=0
for i in range(len(mylist)):
    if (i+1)%2==0:
        mysum+=mylist[i]
    if (i+1)%3==0:
        mysum2+=mylist[i]
        count+=1
print(mysum,end=" ")
print(f"{mysum2/count:.1f}")
