mylist=list(map(int,input().split()))
n=mylist.index(0)
#print(n)
new_list=[mylist[i] for i in range(n)]
#print(new_list)

sum1=0
for i in range(1,4):
    sum1+=new_list[-i]
print(sum1)