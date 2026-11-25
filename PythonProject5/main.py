#python compound interest calculator
principle = 0
rate = 0
time = 0

#while True:
    #principle = float(input("Enter the principle amount: "))
    #if principle <0:
        #print("principle cant be less than zero.")
    #else:
        #break

#while True:
    #rate = float(input("Enter the interest rate: "))
    #if rate <0:
        #print("interest rate cant be less than zero.")
    #else:
        #break

#while True:
    #time = int(input("Enter the time in years: "))
    #if time <0:
        #print("time cant be less than zero.")
    #else:
       # break

#total = principle * pow((1 + rate / 100), time)

#print(f"Balance after {time} year/s: £{total:.2f}")


#For loops = executes block of code a fixed number of times


#for x in reversed(range(1,11,2)):
    #print(x)

#print("Happy New year!")

#credit_c = input(f"Enter credit card number")

#for x in credit_c:
    #print(x)

#for x in range(1,21):
    #if x == 13:
        #break
    #else:
        #print(x)

#for x in range(1,21):
    #if x == 13:
        #break
    #else:
        #print(x)




#making a countdown timer

#import time

#my_time = int(input("How long would you like to set the timer for in seconds?"))

#for x in reversed(range(0, my_time)):
    #seconds = x % 60
    #minutes = int(x / 60) % 60
    #hours = int((x / 60) / 60)
    #if x == 0:
        #break
    #else:
        #print(f"{hours:02}:{minutes:02}:{seconds:02}")
        #time.sleep(1)


#print("timer done!")



#nested loops is a loop within a loop (outer, inner)
#               outer:
#                   inner:


#rows = int(input("enter the number of rows: "))
#columns = int(input("enter the number of columns: "))
#symbol = input("enter a symbol for the rectangle to be made out of: ")

#for x in range(rows):
    #for y in range(columns):
        #print(symbol, end=" ")
    # print()