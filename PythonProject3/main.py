#python calculator

#operator = input("Please, enter an operator. Either +, -, *, /: ")

#num1 = float(input("Please, enter the first number: "))
#num2 = float(input("Please, enter the second number: "))

#if operator == "+":
    #result = num1 + num2
    #print(round(result, 3))
#elif operator == "-":
    #result = num1 - num2
    #print(round(result, 3))
#elif operator == "*":
    #result = num1 * num2
    #print(round(result, 3))
#elif operator == "/":
    #result = num1 / num2
    #print(round(result, 3))
#else:
    #print(f"{operator} is not a valid operator. Please enter a valid operator.")


#Python Weight converter task

#weight = float(input("Enter your weight: "))
#unit = input(f"Is {weight} in lbs or kg? Please enter either L for lbs or K for kg: ")

#if unit == "L":
    #weight = weight / 2.205
    #print(f"Your weight is {round(weight, 2)}kg")
#elif unit == "K":
    #weight = weight * 2.205
    #print(f"Your weight is {round(weight, 2)}lbs")
#else:
    #print(f"{unit} is not valid. Please enter either L or K")



#Temperature converter tool

#temperature = float(input("What is the current temperature?: "))
#unit = input("What unit are you using for this temperature? (C or F): ")

#if unit == "C":
    #temperature = round(9 * temperature, 2) / 5 + 32
    #print(f"The current temperature is {round(temperature, 3)}°F")
#elif unit == "F":
   # temperature = (9 / temperature) / 5 + 32
    #print(f"The current temperature is {round(temperature, 3)}°C")
#else:
   # print(f"{unit} is not a valid unit.")


#logical operators = evaluate multiple conditions(or, and, not)
#           or = at least one condition must be True
#           and = both conditions must be True
#            not = inverts the condition (not False, not True)


#petrol = 20
#money = 40
#no_space = False

#gk_in_stock = True
#frieren_in_stock = True


#if petrol < 10 or no_space or money < 10:
    #print("Sadly, no forbidden plannet today. :( ")
#else:
    #print("Forbidden planet is still on the cards! :) ")


#if gk_in_stock and frieren_in_stock:
  #  print("Frieren is in stock, lets go!")
   # print("Golden Kamuy is in stock, lets go!")
#elif gk_in_stock:
  #  print("Golden Kamuy is in stock, lets go!")
   # print("Frieren is not in stock :( ")
#elif frieren_in_stock:
    #print("Frieren is in stock, lets go!")
   # print("Golden Kamuy is not in stock :( ")
#elif not frieren_in_stock and not gk_in_stock:
    #print("Neither are in stock, ets save it for another day!!")



#conditional expressions = A one line shortcut for the if-else statement (ternary operator)
#               print or assign one of two values based on a countdown
#               X if condition is true, else Y

#manga_stock = 10
#print("In stock" if manga_stock > 0 else "Not in stock")

#goals = 3
#print("goals have been scored" if goals > 0 else "Goals have not been scored")

#number = 3
#print("number is even" if number % 2 == 0 else "Number is odd")

#a = int(input("Please enter a number (this number will be called a: "))
#b = int(input("Please enter a number (this number will be called b: "))

#max_num = a if a > b else b
#min_num = a if a < b else b
#print(f"The heighest number was {max_num}")
#print(f"The lowest number was {min_num}")

#age = int(input("Please enter your age: "))
#age_range = "adult" if age >= 18 else "child"
#print(f"You are a {age_range} due to you being {age} years old")

#temp = float(input("What is the temperature in °C?: "))
#heat_range = "It is hot" if temp >= 15 else "It is cool"

#print(heat_range)

#clearance_lvl = "admin"

#access_level = "You can enter this room" if clearance_lvl == "admin" else "You do not have the clearance to enter this room"
#print(access_level)

#biscuits = 0
#biscuits_left = "you have some biscuits left" if biscuits == 1 else "you have some biscuits right"
#print(biscuits_left)





