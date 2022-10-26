num = int(input("Enter any number to check its armstrong no or not\n"))
temp = num

print(num)
sum = 0
rem = 0
while(num > 0):
    rem = num % 10
    sum += (rem * rem * rem)
    num = num // 10

if(sum == temp):
    print(f"{temp} is armstrong number")
else:
    print(f"{temp} is not an armstrong number")