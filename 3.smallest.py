list = [10,8,1,6,4,5,2,-1,-5]
smallest = list[0]
for x in range(1,len(list)):
    if smallest > list[x]:
        smallest = list[x]
print(smallest)