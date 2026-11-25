#collections = single "variable" used to store multiple values
# List = [] ordered and changeable. Allows duplicate members.
# set = {} unordered, unidexed and ummutable, but add/remove ok. no duplicates
# tuple = () ordered and unchangeable. Allows duplicate members. faster


#LISTS ------------------------------------------------------------
#weapons = ["sword", "wand", "polearm", "axe", "scythe"]

#print(dir(weapons))
#print(help(weapons))
#print(len(weapons))  SHOWS THE LENGTH OF THE LIST, NOT CHARACTERS
#print("polearm" in weapons)

#weapons[0] = "dagger"

#weapons.append("staff") #ADDS SOMETHING TO THE END OF THE LIST
#weapons.remove("axe") #REMOVES SOMETHING FROM THE LIST
#weapons.insert(0, "staff") #ADDS SOMETHING TO THE LIST DEPENDING ON THE INDEX
#weapons.sort() #ORDERS THE LIST IN ALPHABETICAL ORDER
#weapons.reverse() #REVERSES THE ORDER OF THE LIST FROM THE ORIGINAL ORDER YOU PLACED IT IN
#weapons.clear()
#print(weapons.index("wand")) #TELLS YOU THE INDEX OF THE STRING IN THE LIST
#print(weapons.count("axe")) #TELLS YOU NUMBER OF TIMES THAT STRING APPEARS IN THE LIST

#for weapon in weapons:
    #print(weapon)

#SET-----------------------------------------------------------------------------------------------

#weapons = {"sword", "wand", "polearm", "axe", "scythe"}
#print(dir(weapons))
#print(help(weapons))
#print(weapons)
#weapons.add("scissors")
#weapons.remove("axe")
#weapons.pop() # REMOVES FIRST ELEMENT BUT IN A SET, FIRST ELEMENT IS RANDOM SO IT RANDOMLY REMOVES AN ELEMENT
#weapons.clear
#print(weapons)

#TUPLE---------------------------------------------------------------------------------------------------
#weapons = ("sword", "wand", "polearm", "axe", "scythe")
#print(dir(weapons))
#print(help(weapons))
#print(len(weapons))

#print(weapons.index("axe"))
#print(weapons.count("axe"))
#print(weapons)

#for weapon in weapons:
    #print(weapon)



#SHOPPING CART PROGRAMME

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    food = food.lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: £"))
        foods.append(food)
        prices.append(price)

print("----- YOUR SHOPPING CART -----")
for food in foods:
    print(food, end= ", ")


for price in prices:
    total += price

print()
print(f"Your overall total is {total}")
