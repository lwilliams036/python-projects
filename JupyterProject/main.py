#different types of string methods
from numpy.f2py.auxfuncs import process_f2cmap_dict

#name = input("Enter your name please: ")

#result = len(name)
#result = name.find("l") #finds the first occurance of the character in the bracket
#result = name.rfind("l") #finds the last occurance of the character in bracket
#result = name.lower() #puts all in lower case
#result = name.capitalize() #makes first character a capital letter in the string
#result = name.upper() #makes all characters upper case
#result = name.isdigit() #checks if all characters are digits in the string, if so = true
#result = name.isalpha() #checks if the string only contains the alphabet, if so returns true

#phone_number = input("Enter a phone number: ")
#result = phone_number.count("-") #this counts the amount of times the character in bracket is used
#result = phone_number.replace("-", " ") #replaces one character with another
#print(result)


#Username with limitations task!



#username = input("Enter a 12 letter username without any spaces or numbers: ")
#if username.count("") > 12:
    #print("Your username is too long. 12 letter MAX!!")
#elif not username.find(" ") == -1:
    #print("Your username contains spaces. NO SPACES!!")
#elif username.isalpha() == False:
    #print("Your username must contain only alphanumeric characters. NO OTHER CHARACTERS!!")
#else:
    #print(f"your username is {username.replace(" ", "")}!")



# indexing is accessing different elements of a sequence using [] (indexing operator)
        #[start : end : step]

#credit_number = "1234-5678-9012-3456"

#print(credit_number[0]) #start
#print(credit_number[:4]) #end
#print(credit_number[5:9])
#print(credit_number[5:])
# print(credit_number[-1]) negative index starts from the opposite end of the string
#print(credit_number[0:10:2])

#c_card = input("Please enter your card number: ")
#c_card = c_card.replace(" ", "")
#c_card = c_card.replace("-", "")
#print(f"The last 4 digits of your card are {c_card[-4:]}, correct?")
#print(c_card[::-1])



#format specifiers = {:flags} format a value based on what flags are inserted
#flags!
#:.2f = 2 decimal places for a float
#:10 pads a string with space so the string is 10 characters
#:010 the padding is now with 0s instead of just space
#:<10 the padding space is all to the right of the string
#:>10 the padding is to the left of the string
#:^10 the padding is around each side of the number, centering the number
#:+ adds a plus sign to a positive value OR leave a space instead of a + to allow positive and negative numbers to line up evenly
#:, separates 1000s. 1000 becomes 1,000




#price1 = 3000.14159
#price2 = -9870.65
#price3 =1200.34

#print(f"Price 1 is £{price1:+,.2f}")
#print(f"Price 2 is £{price2:+,.2f}")
#print(f"Price 2 is £{price3:+,.2f}")



#while loops = excecutes code WHILST something is true

#name = input("please enter your name: ")
#while name == "":
    #print("you did not enter your name :( ")
    #name = input("please enter your name: ")
#else:
    #print(f"Hello, {name}, nice to meet you :)")

#age = int(input("Please enter your age: "))
#while age < 0:
    #age = int(input("You cant be negative years old. Please enter your age: "))
#else:
    #if age == 0:
        #print("You have just been born.")
    #elif 0 < age <= 17:
        #print("You are a child.")
    #else:
        #print("You are an adult.")
#print(f"You are {age} years old!")


#manga = input("Please, enter your favourite manga (q to quit): ")
#while not manga == "q":
    #print(f"You like {manga}")
    #manga = input("Please, enter another manga that you like (q to quit): ")
#else:
    #print("Thank you, goodbye!")

#anime = input("What is your favourite anime? (enter l to quit): ")
#anime = anime.lower()
#while not anime == "l":
    #print(f"You have entered {anime}.")
    #anime = input("Please enter another. (or l to quit): ")
#else:
    #print("Thank you. Goodbye!")

#my first propper working while loop

#num = input("Enter a number between 1 and 1000: ")
#while not num.isdigit():
   # print(f"{num} is not a valid number. Try again.")
   # num = input("Enter a number between 1 and 1000: ")
#num = int(num)
#while num > 1000 or num < 1:
   # print(f"{num} is not a valid number. Enter a number between 1 and 1000.")
   # num = input("Enter a number between 1 and 1000: ")
   # while not num.isdigit():
        #print(f"{num} is not a valid number. Try again.")
       # num = input("Enter a number between 1 and 1000: ")
  #  num = int(num)
#else:
    #while 1000 > num > 0:
       # ans = input(f"The number you have chosen is {num}. Again? Y or N.")
      #  if ans == "Y" or ans == "y":
            #num = input("Enter a number between 1 and 1000: ")
           # while not num.isdigit():
               # print(f"{num} is not a valid number. Try again.")
               # num = input("Enter a number between 1 and 1000: ")
           # num = int(num)
       # elif ans == "N" or ans == "n":
           # print("Okay, Have a nice day!")
           # break
       # else:
           # print("An invalid answer was entered, try again.")

token = 0
book = input("Please enter the book you want to buy? (Or leave blank if you would like to exit) ")
while not book == "":
    print(f"The book you have chosen is {book}!")
    ans1 = input("Is this correct? (y/n) ")
    ans1 = ans1.lower()
    if (ans1 == "y"):
        token = token + 1
        print("Perfect!")
        break
    elif (ans1 == "n"):
        print(f"You have chosen {ans1}!")
        book = input("Please enter the book you want to buy? (Or leave blank to exit) ")
    elif (ans1 == ""):
        print("Oi, no leaving this one blank, you missed your chance to exit!")
        print("Please try again!")
    else:
        print(f"{ans1} was an invalid answer, please try again!")
else:
    print("Thanks for nothing ig.")

if token > 0:
    volume_count = input("How many volumes would you like? ")
    while not volume_count.isdigit():
        if volume_count == "":
            print("Oi, no leaving this one blank, you missed your chance to exit!")
        else:
            print(f"{volume_count} is an invalid option, please try again!")
        volume_count = input("How many volumes would you like? ")
    volume_count = int(volume_count)
    while volume_count <= 0:
        print(f"{volume_count} is an invalid number, please try again!")
        volume_count = input("How many volumes would you like? ")
        while not volume_count.isdigit():
            print(f"{volume_count} is an invalid option, please try again!")
            volume_count = input("How many volumes would you like? ")

        volume_count = int(volume_count)
    print(f"You have entered {volume_count} volumes!")
    ans2 = input("Is this correct? (y/n) ")
    ans2 = ans2.lower()
    while token == 1 :
        if (ans2 == "y"):
            print(f"Perfect, {volume_count} volume/s coming up!")
            token = token + 1
            break
        elif (ans2 == "n"):
            print(f"You have chosen {ans2}!")
            volume_count = input("Please enter the number of volume/s you want to buy? ")
            while not volume_count.isdigit() or int(volume_count) <= 0:
                print(f"{volume_count} is an invalid number, please try again!")
                volume_count = input("Please enter the number of volume/s you want to buy? ")

            volume_count = int(volume_count)

            print(f"You have entered {volume_count} volumes!")
            ans2 = input("Is this correct? (y/n) ").lower()

        elif (ans2 == ""):
            print("Oi, no leaving this one blank, you missed your chance to exit!")
            ans2 = input(f"You have entered {volume_count} volume/s. Is this correct? (y/n) ")

        else:
            print(f"{ans2} is an invalid answer, please try again!")
            print(f"You have entered {volume_count} volumes!")
            ans2 = input("Is this correct? (y/n) ")

if token == 2:
    print(f"You have recieved {volume_count} volume/s of {book}!")














