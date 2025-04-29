a = input()
num=list(a)

for i in range(len(num)):
    if num[i]=="0":
        num[i]="1"
        break

sum=0
k=0
for i in range(len(num)-1,-1,-1):
    sum+=(int(num[k])*(2**i))
    #print(sum)
    k+=1
print(sum)

