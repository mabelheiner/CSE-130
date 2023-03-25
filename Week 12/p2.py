import math
number = int(input("Enter the max number: "))

check = int(math.sqrt(number))

print(check)

null = -1

num_list = []
for i in range(1, number + 1):
    num_list.append(i)
    
for num in range(len(num_list)):
    if num_list[num]%2 == 0:
        num_list[num] = -1
        
for number in range(len(num_list)):
    if num_list[number] != -1:
        print(num_list[number])