limit = int(input("Enter a number till where you want to print fibonacii series\n"))
a, b = 0, 1
c = 0
print(a)
while(c <= limit):
    c = a+b
    print(b)
    a,b = b,c

