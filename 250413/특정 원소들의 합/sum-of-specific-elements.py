matrix=[list(map(int,input().split()))for _ in range(4)]
count=0
total=0
for row in matrix:
    count+=1
    for i in range(count):
        total+=row[i]
print(total)