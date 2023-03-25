import json

file = input("Please enter a file of words: ")
data = open(file)
word_list = json.load(data)
data.close()

words = word_list['array']

count = 0

i_check = "/"
print("\tPivot \tLargest Check \tWords")
print("______________________________________")
#goes through the list in reverse order
for i_pivot in range(len(words)-1, 0, -1):
    #largest is the first one
    i_largest = 0
    count = "A"
    
    print(count, "\t", i_pivot, i_largest, i_check, words)
    print("______________________________________")
    
    #check is the second one
    for i_check in range(1, i_pivot+1):
        #checks if the following one is larger than the first
        if words[i_check] > words[i_largest]:
            i_largest = i_check
         
        count = "B"    
        print(count, "\t", i_pivot, i_largest, i_check, words)
        print("______________________________________")
    
    count = "C"    
    print(count, "\t", i_pivot, i_largest, i_check, words)
    print("______________________________________")
    #adjusts the pivot and locks in the largest
    words[i_pivot], words[i_largest] = words[i_largest], words[i_pivot]    
    
count = "D"
print(count, "\t", i_pivot, i_largest, i_check, words)
print(words)