numbers = [2,2,2,2,2,2]
even_count = 0
odd_count = 0
for i in numbers:
    if(i%2):
        odd_count+=1
    else:
        even_count+=1
print(f"IN list {even_count} is even_numbers\nIN list {odd_count} is odd_numbers")