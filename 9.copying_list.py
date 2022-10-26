#copying list without using inbuilt functions
list = [111, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#list1 = []
# len=len(list)     #not working
# for x in range(0, len):
#     list1[x] = list[x]
#     print(x)
# print(list1)

# i=0
# for x in list:     #not working brush up concepts
#     list1[i] = x
#     i+=1
# print(list1)

# i=0
# for x in list:   #working every time appending element at last
#     list1.append(x)
#     i+=1
# print(list1)

list1 = list.copy()          #working using inbuilt function
print(list1)

