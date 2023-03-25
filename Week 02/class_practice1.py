# 1. Name:
#      Mabel Heiner
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      -describe what this program is meant to do-
#      This program reads in logins from a json files and checks
#      for a valid login from the user. If the username and password
#      match, the user will be authorized, otherwise the user will not
#      be authorized. 
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
#      Checking for the match of the username and password was the hardest
#      part. I was just checking for if the username and password were in 
#      the list, but I needed the specific username to match with a specific
#      password. I used an index to solve this problem. 
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
#      This program took me about 2 hours. This includes 30 minutes of reading and planning,
#      15 minutes of research, 1 hour of programming, 15 minutes of editing and videoing. 

import json 

def main():
    with open('name.txt', 'w') as file:
        file.write("Mabel")
    
    with open("name.txt", "r") as name_src:
        name = name_src.read()
               
    print(name)
        
          
if __name__ == "__main__":
    main()