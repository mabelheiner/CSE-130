# 1. Name:
#      Mabel Heiner
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. Algorithmic Efficiency
#      -Identify the algorithmic efficiency and tell why it is as you say it is-
#       The efficiency here is log n as by using the middle index, we get rid of 
#       have the possibilities. 
# 5. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
#       The hardest part was figuring out how to adjust the middle index.
# 6. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
#       This assignment took me 3 hours. 30 minutes reading the description. 2 hours programming
#       the solution and finding out the algorithm. 30 minutes to figure out the efficiency. 

import sys
import json

filename = input("Enter a filename: ")

data = open(filename)
word_list = json.load(data)

words = word_list["array"]

word = input("Enter a word to search for: ");

if len(words) == 0:
    print("cannot find word")
    sys.exit()
    
mid = int(len(words) / 2);

while word != words[mid]:
        print(mid)
        print(word)
        print(words[mid])
        print("Total length: ", len(words))
        if mid == len(words) - 1:
            print("cannot find word")
            sys.exit()
        
        if word > words[mid]:
            mid += 1
            continue
        elif word < words[mid]:
            mid = int(mid / 2)
            continue
        else:
            print("cannot find word")
            sys.exit()
print("found word!")