# from array import *
# array1 = array('i', [5,4,3,2,1])
# temp = 0
# for x in array1:
#     if(x > x+1):
#         temp = x
#         x = (x+1)
#         (x+1) = temp

from array import *
vals = array('i', [5,4,3,2,1])
new_Arr = array(vals.typecode, (a for a in vals))

for a in new_Arr:
    print(a)