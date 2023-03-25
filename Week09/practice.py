response = open("BOM_NoPunc.txt")
data = response.read()
data_list = data.split(" ")

dictionary = {}

for word in data_list:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
        
print(dictionary)