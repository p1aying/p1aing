a=[0 for i in range(3)]
b=[0 for i in range(3)]
a[0],b[0]=map(str,input().split())
a[1],b[1]=map(str,input().split())
a[2],b[2]=map(str,input().split())
count=0
for i in range(3):
    if a[i]=="Y" and int(b[i])>=40:
        print("E")
        count+=1
        break
    else:
        continue
if count==0:
    print("N")