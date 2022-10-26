

#clearing list using list clear function
list = [1,2,3,4,5,6,7,8,9]
#list.clear()
#print(list)

#another way to delete list
#del list[0:]


#another way to delete list using len
for x in range(len(list)):
    list.pop()
print(list)


