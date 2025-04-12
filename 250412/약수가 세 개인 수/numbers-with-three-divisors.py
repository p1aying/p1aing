start, end = map(int, input().split())
count=0
num_list=[]
for i in range(start,end+1):
    for j in range(1,i+1):
        if i%j==0:
            num_list.append(j)
            #print(set(num_list))
    if len(num_list)==3:
        #print(num_list)
        num_list=[]
        count+=1
    else:
        num_list=[]
print(count)
    
    