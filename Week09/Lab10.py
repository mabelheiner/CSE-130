# 1. Name:
#      Mabel Heiner
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program creates a list of numbers that is a length determined
#      by the user. This list will be appended with a number that is the 
#      sum of the previous two numbers.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out where to put the asserts.
#      The first assert is to make sure that each number is bigger in the list.
#      The second assert is to make sure that the list is created to the right
#      length.
# 5. How long did it take for you to complete the assignment?
#      This assignment took me 3 hours. 1 hour was creating the initial formation
#      and appending to the list properly. 1 hour was adding in the asserts and 
#      other checks like making sure the program had proper input. The last hour
#      was filming the video and adding in the main if statement as I previously
#      had the program importing sys and then doing sys.exit().

num = int(input("Which Francois number would you like to see: "))

while num < 1:
    print("Please enter a number greater than 0.")
    num = int(input("Which Francois number would you like to see: "))

index = 2
num_list = [2, 1]

if num == 1:
    print(f"The Francois number {num} is {num_list[num - 1]}")
    
elif num == 2:
    print(f"The Francois number {num} is {num_list[num - 1]}")

else:
    while index < num:
        new_num = num_list[index-2] + num_list[index-1]
        num_list.append(new_num)
        index += 1
    
    assert num_list[-1] > num_list[-2], "Incorrect Francois number"
    assert len(num_list) == num, "Incorrect number of Francois numbers"
    
    print(f"The Francois number {num} is {num_list[-1]}")