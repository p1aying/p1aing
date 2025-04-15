n=int(input())
count=0
for i in range(1,n+1):
    new_num=list(str(i))
    if i%3==0:
        print(0, end=" ")
        new_list=[]
    else:
        for ii in range(len(new_num)):
            if new_num[ii]==("3" or "6" or "9"):
                print(0, end=" ")
                count+=1
                break
        if count==0:
            print(i,end=" ")
        count=0
        new_list=[]