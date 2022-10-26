list = [10,8,199,1,6,4,5,2,-1,-5, 180, 1845, 189]
largest = list[0]
sec_lar = 0
for x in range(1,len(list)):
    if largest < list[x]:
        sec_lar = largest
        largest = list[x]
    elif sec_lar != largest and list[x] > sec_lar:
        sec_lar = list[x]
print(sec_lar)