# example for continue
num = int(input("Enter any number\n"))
i=0
while(i<num):
    i=i+1
    if(i == 5):
        continue
    print(i)


# example for break
#it will break whole loop and control will come out of the loop
print('\n\n')
i=0
while(i < 10):
    i=i+1
    if(i == 5):
        break
    print(i)
