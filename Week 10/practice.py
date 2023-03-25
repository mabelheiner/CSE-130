number = int(input("What number do you want to sum up? "))

num = 0
sum = 0
nums = []

while num <= number:
    nums.append(num)
    sum += num
    num += 1
    
print("The sum is", sum)
print("The loop used", nums)