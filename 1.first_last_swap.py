list = ["Arun",20,30,40,50,"Deore"]
temp = list[0]
list[0] = list[-1]
list[-1] = temp
print(list)