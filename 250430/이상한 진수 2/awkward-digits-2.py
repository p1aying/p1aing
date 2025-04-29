a = input()
num=list(a)
sum_list=[]
sum=0
for i in range(len(num)):
    if num[i]=="0":
        num[i]="1"
        k=0
        for i in range(len(num)-1,-1,-1):
            sum+=(int(num[k])*(2**i))
            #print(sum)
            k+=1
        sum_list.append(sum)
        sum=0
    elif num[i]=="1":
        num[i]="0"
        k=0
        for i in range(len(num)-1,-1,-1):
            sum+=(int(num[k])*(2**i))
            #print(sum)
            k+=1
        sum_list.append(sum)
        sum=0
    num=list(a)
    #print(num)
print(max(sum_list))

