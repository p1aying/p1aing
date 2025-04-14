n=int(input())
my_list=list(map(int,input().split()))
new_list=[]
for i in range(len(my_list)):
    if my_list[i]%2==0:
        new_list.append(my_list[i])
    else:
        continue
for i in range(len(new_list)):
    n=new_list.pop()
    print(n, end= " ")