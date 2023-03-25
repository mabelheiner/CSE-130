import json

file = input("What is the file name? ")

data = open(file)

nums = json.load(data)

data.close()

print(nums)

rev_nums = []
for i in range(len(nums)):
    rev_nums.append(nums.pop(-1))
    
print(rev_nums)
print(nums)