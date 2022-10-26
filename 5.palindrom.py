num = int(input("Enter a number\n"))
temp = num
res = 0
while(num > 0):
    rem = num % 10
    res = res * 10 + rem
    num = num // 10

if(res == temp):
    print(f"{res} is palindrome number")
else:
    print(f"{temp} is not palindrome number")

