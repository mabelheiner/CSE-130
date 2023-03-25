# 1. Name:
#      Mabel Heiner
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program takes in a file with a list and sorts it in order.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was figuring out where to put the asserts.
#      I put asserts to check if the file is a JSON file. The second assert is to make sure
#      that the file can be opened. The third assert is to check if the i_check and the i_largest
#      are the same type so that the python built-in ">" comparison can work. 
# 5. How long did it take for you to complete the assignment?
#      This assignment took me 4 hours. 2 hours in coding. 1 hour in successfully placing the asserts. 30 minutes of testing.
#      30 minutes of filming. 

import json
import os

def sort_file(file):
    assert os.path.splitext(file)[1] == ".json", "file must be a JSON file"
    
    try:
        data = open(file)
        
    except:
        assert False, "Unable to open file. Check file name."
        
    word_list = json.load(data)
    data.close()

    words = word_list['array']

    #goes through the list in reverse order
    for i_pivot in range(len(words)-1, 0, -1):
    #largest is the first one
        i_largest = 0
    
    #check is the second one
        for i_check in range(1, i_pivot+1):
        #checks if the following one is larger than the first
            assert type(words[i_check]) == type(words[i_largest]), "all values in the file must be the same type"
            
            if words[i_check] > words[i_largest]:
                i_largest = i_check
    #adjusts the pivot and locks in the largest
        words[i_pivot], words[i_largest] = words[i_largest], words[i_pivot]    
    
    print("The values in the", file, "are:")
    for item in range(len(words)):
        print("\t", words[item])
        
    print()
    
def main():
    
    file = None
    while file != "q":
        file = input("What is the name of the file? ")
        sort_file(file)
        
if __name__ == "__main__":
    main()