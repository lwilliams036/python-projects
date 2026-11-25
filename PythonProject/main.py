# Variable is a cvontainer for a value, including things like a string, integer, float and boolean
# they behave as if it is the value it contains

#strings ONLY STRINGS NEED QUOTATION MARKS
first_name = "luke"
food = "bao buns"
email = "luke656@fake.com"


#Integers
age = 19
cost_usually = 12
scam = 5


#floats
height = 6.2
cost_now = 10.99
money_lost = 25.11

#booleans
rank = False
manga_sale = True

print(f"Hello {first_name}, you are {age} years old. You are also {height} feet tall.")
print(f"Usually, {food} costs around £{cost_usually} but recently it costs {cost_now}.")
print(f"You shouldnt tell everyone that your email is {email}, that is why you have been scammed {scam} times!")
print(f"that is also why you are down {money_lost} to these nigerian princes.")
print(f"How true is it that your marvel rivals rank is plat? {rank}")

length = float(input("Enter a length: "))
heightT = float(input("Enter a height: "))
heightT = int(heightT)
area = length * heightT / 2

print(f"the area is {area} cm²")

if rank == True:
    print(f"Your rank is Plat")
else:
    print(f"Your rank is Not Plat")

if manga_sale == True:
    print(f"Manga is for sale")
else:
    print(f"Manga is not for sale")

if cost_now > 15:
    print(f"{food} are expensive, maybe hold off from buying it!")
else:
    print(f"Buy the {food} now!")



#changing one type of variable into a different type below
height = int(height)
print(height)

age = float(age)
print(age)


#input() is a function that gets the user to enter data


#fav_manga = input("What is your favourite manga?: ")
#print(f"you have chosen {fav_manga} as your favourite manga.")

#tru_fal = input("if this is correct, type True, if not, type False")
#if tru_fal == "True":
    #print("Nice choice!")
#elif tru_fal == "False":
    #fav_manga = input("What is your favourite manga?: ")
#else:
    #print("Sorry, I can't do that.")

