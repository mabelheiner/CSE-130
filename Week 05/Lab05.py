import sys
import json

filename = input("Enter a filename: ")

data = open(filename)
word_list = json.load(data)
print(word_list)

words = word_list["array"]

word = input("Enter a word to search for: ");

mid = int(len(words) / 2);

while word != words[mid]:
        if mid == len(words) - 1:
            print("cannot find word")
            sys.exit()
        '''    
        print("mid", mid)
        print("word", word)
        print("middle word", words[mid])
        print("total length", len(words))
        '''
        
        if word > words[mid]:
            #print("greater")
            mid += 1
            continue
        else:
            #("print lesser")
            mid = int(mid / 2)
            continue

print("found word!")