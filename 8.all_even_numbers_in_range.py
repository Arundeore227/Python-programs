num = int(input("Enter a number\n"))
print(f"Even number from 0 to {num} are: ", end= " ")
for i in range(0, num+1):
    if i%2 == 0:
        print(i, end=" ")