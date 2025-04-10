a=["apple","banana","grape","blueberry","orange"]
b=input()
cnt=0
for x in a:
    if x[2]==b or x[3]==b:
        print(x)
        cnt+=1
print(cnt)