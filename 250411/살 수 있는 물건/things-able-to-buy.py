money=int(input())

book=3000
mask=1000

if money>=book:
    print("book")
elif book>money>=mask:
    print("mask")
else:
    print("no")