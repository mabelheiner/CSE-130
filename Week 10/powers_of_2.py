number = int(input("Enter in a number: "))

num_list = []

for num in range(1, number+1):
    num_list.append(number**num)
    
print(num_list)