Arr = list(map(int,input("Enter array Elements: ").split()))
print(f"array elements are :{Arr}")

new_Arr = []
for i in range(0, len(Arr)):
    minimum = Arr[0]
    for k in Arr:
        if k < minimum:
            minimum = k
    new_Arr.append(minimum)
    Arr.remove(minimum)
print(f"Array elemets after sorting are\n {new_Arr}")