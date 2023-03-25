import math

limit = int(input("Please enter a number: "))

numbers = []

for n in range(2, limit+1):
    numbers.append(n)

index = 0
while numbers:
    prime = numbers[index]
    print(prime)
    index += 1

    for n in range(prime*2, limit+1, prime):
        if n in numbers:
            numbers.remove(n)
        
print(numbers)