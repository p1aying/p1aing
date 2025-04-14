a=[0 for i in range(3)]
b=[0 for i in range(3)]
a[0],b[0]=map(str,input().split())
a[1],b[1]=map(str,input().split())
a[2],b[2]=map(str,input().split())
count=0
for i in range(3):
    if (a[i]=="Y" and int(b[i])>=37):
        count+=1
    else:
        continue
if count>=2:
    print("E")
else:
    print("N")