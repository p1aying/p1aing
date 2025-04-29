a = input()
num = list(a)

for i in range(len(num)):
    if num[i] == "0":
        num[i] = "1"
        break

binary_str = ''.join(num)
print(int(binary_str, 2))
