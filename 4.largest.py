list = [3000,10,8,199,1,6,4,5,2,-1,-5, 180,2000, 1845, 189]
largest = list[0]
for x in range(1,len(list)):
    if largest < list[x]:
        largest = list[x]
print(largest)