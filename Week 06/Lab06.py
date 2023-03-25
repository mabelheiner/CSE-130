# 1. Name:
#      Mabel Heiner
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#       This program searches for a word given by the user inside a JSON file chosen by the user.
# 4. Algorithmic Efficiency
#       The efficiency here is log n as by using the middle index, we get rid of 
#       half the possibilities and quickly narrow down our search. 
# 5. What was the hardest part? Be as specific as possible.
#       The hardest part was figuring out how to adjust the middle index each time. 
#       Another tricky part was checking for the length of the word if two words started
#       the same way.
# 6. How long did it take for you to complete the assignment?
#       This assignment took me 3 hours. 30 minutes reading the description. 2 hours programming
#       the solution and finding out the algorithm as well as filming. 30 minutes to figure out 
#       the efficiency. 

import sys
import json

filename = input("Enter a filename: ")

data = open(filename)
word_list = json.load(data)
data.close()

words = word_list["array"]

word = input("Enter a word to search for: ");

first = 0
last = len(words)

found = False

if len(words) == 0:
    print("cannot find word")
    sys.exit()

num = 0
print("\t First\tLast\tMiddle")
while first <= last and found != True:
    middle = int((first + last) / 2) 
    
    print("----------------------------------------------------------------")
    print(num, "\t", words[first], "\t", words[last - 1], "\t", words[middle])
    num += 1
   
    if words[middle] < word:
        first = middle + 1
        continue
    elif words[middle] > word:
        last = middle - 1
        continue
    else:
        if len(word) == len(words[middle]):
            found = True
            break
        else:
            found = False
            continue
        
print("----------------------------------------------------------------")
print(num, "\t", words[first], "\t", words[last - 1], "\t", words[middle])    

if found != True: 
    print("cannot find word")   
    
else:      
    print("found word")
    
