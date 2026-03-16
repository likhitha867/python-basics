x = 153
y = len(str(x))  
sum = 0
temp = x      

while temp > 0:
    digit = temp % 10
    num = digit ** y
    sum += num
    temp = temp // 10

print(sum)