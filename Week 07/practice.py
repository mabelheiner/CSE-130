number = int(input("Please enter a positive number: "))

sum = 0

print("\t Number\tCount\tSum ")

for count in range(1, number + 1):
    sum += count
    print("B\t", number, "\t", count, "\t", sum)
    

print("the sum is: ", sum)

