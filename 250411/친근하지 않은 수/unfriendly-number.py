a=[x for x in range(1,int(input()))]
b=[]

for i in range(len(a)):
    if (a[i]%2==0) or (a[i]%5==0) or (a[i]%3==0):
       b.append(a[i]) 
    else:
        continue
print(len(a)-len(b))
