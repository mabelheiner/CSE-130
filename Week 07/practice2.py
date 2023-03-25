import json

file = input("Please enter a file of words: ")
data = open(file)
word_list = json.load(data)
data.close()

words = word_list["array"]
print(words)

print("\tLargest\tPivot\tCheck")
count = 0
#goes through the list in reverse order
for i_pivot in range(len(words)-1, 0, -1):
    #largest is the first one
    i_largest = 0
    count += 1
    
    #check is the second one
    for i_check in range(1, i_pivot+1):
        #checks if the following one is larger than the first
        if int(words[i_check]) > int(words[i_largest]):
            i_largest = i_check
        print("__________________________________")
        print(count, "\t", i_largest, "\t", i_pivot, "\t", i_check)
        print(count, "\t", words[i_largest], "\t", words[i_pivot], "\t", words[i_check])
        print(count, "\t", words)
        
    
    #adjusts the pivot and locks in the largest
    words[i_pivot], words[i_largest] = words[i_largest], words[i_pivot]
    print("__________________________________")
    print(count, "\t", i_largest, "\t", i_pivot, "\t", i_check)
    print(count, "\t", words[i_largest], "\t", words[i_pivot], "\t", words[i_check])
    print(count, "\t", words)
    
    

print(words)