list = [1,2,3,4,5,1,1,2,3,4,5,6,7]
num = int(input("ENter a number whose occurance you want to count\n"))
count = 0
for x in list:
    if num == x:
        count += 1
print(f"{num} repeted {count} times in list")