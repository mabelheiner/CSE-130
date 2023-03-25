# 1. Name:
#      Mabel Heiner
# 2. Assignment Name:
#      Lab 04: Monopoly Program
# 3. Assignment Description:
#      This program determines if and how much it would be to put a 
#      hotel on the property, Pennsylvania Avenue, in the game: Monopoly.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out all the purchase output options. 
#      I had a difficult time determining when each one would be triggered.
# 5. How long did it take for you to complete the assignment?
#      I spent about 30 minutes planning this assignment and looking at the 
#      two flowcharts. I spend 90 minutes programming this scenario. I spent 
#      45 minutes filming the video and testing the test cases. 
import sys

owned = input("Do you own all the green properties? (y/n) ")
if owned == "y":
    pc_curr = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
else:
    print("You cannot purchase a hotel until you own all the properties of a given color group.")
    sys.exit()
    

if pc_curr < 5:
    pc_need = 4 - pc_curr

else:    
    print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
    sys.exit()

nc_curr = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))

if nc_curr < 5:
    nc_need = 4 - nc_curr
    
else:
    print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
    sys.exit()

pa_curr = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
if pa_curr < 5:
    pa_need = 4 - pa_curr
else:
    print("You cannot purchase a hotel if the property already has one.")
    sys.exit()
    
    
num_houses = pa_need + nc_need + pc_need

cost = (num_houses * 200) + 200

curr_money = int(input("How much cash do you have to spend? "))

if curr_money < cost:
    print("You do not have sufficient funds to purchase a hotel at this time.")
    sys.exit()
    
bank_houses = int(input("How many houses are there to purchase? "))
if num_houses > bank_houses:
    print("There are not enough houses available for purchase at this time.")
    sys.exit()

bank_hotels = int(input("How many hotels are there to purchase? "))
if bank_hotels < 1:
    print("There are not enough hotels available for purchase at this time.")
    sys.exit()
    
if pc_need > 0 and nc_need > 0:
    print(f"This will cost ${cost}.\n\tPurchase 1 hotel and {num_houses} house(s).\n\tPut 1 hotel on Pennsylvania and return any houses to the bank.\n\tPut {nc_need} house(s) on North Carolina.\n\tPut {pc_need} house(s) on Pacific.")

elif pc_need > 0:
    print(f"This will cost ${cost}.\n\tPurchase 1 hotel and {num_houses} house(s).\n\tPut 1 hotel on Pennsylvania and return any houses to the bank.\n\tPut {pc_need} house(s) on Pacific.")

elif nc_need > 0:
    print(f"This will cost ${cost}.\n\tPurchase 1 hotel and {num_houses} house(s).\n\tPut 1 hotel on Pennsylvania and return any houses to the bank.\n\tPut {nc_need} house(s) on North Carolina.")

else:
    print(f"This will cost ${cost}.\n\tPurchase 1 hotel and {num_houses} house(s).\n\tPut 1 hotel on Pennsylvania and return any houses to the bank.")



