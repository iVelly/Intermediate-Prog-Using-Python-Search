# Levi Germeil
#
# MidetermPart1
#
# November 7,2022
#
# SE116.01
#
# Prompt: A person asked for a escape from the real world. how is that possible you may ask? A simulation. You must program a simulation
# that tackles everyday life situations such as working, living spaces, groceries and things of that nature.
#
#
#
#
# 
#
# VARIABLE DICTIONARY:
#
# name = The name the user inputs
# jobName = The name of the establishment that the employee works
# wage = the hourly rate an employee
# hoursWK = The amount of hours the employee worked
# gross = "wage" times "hoursWK" give the amount of money accumulated during that time
# totalGross = The amount of money all the employee accumulated during time
# tax = The amount of money uncle sam takes for the state
# totalTax = the amount of tax charged to all employees
# netPay = The amount of money the employee pockets
# totalNetPay = the amount of money all the employees pocket
# bankAccountTotal = The amount of money the employee has in their bank account
# startGame = If this is equal to "Y" it begans the first portion of the program
# showBAT = if this is equal to "Y" it shows the user their bank account total
# tenderedCash = how much cash the user gives the cashier
# changeRecieved = how much change is recieved after transaction
# low = represents the amount the rent cost and in this case, it's 50
# mid = represents the amount the rent cost and in this case, it's 100
# high = represents the amount the rent c ost and in this case, it's 350
# choice =If this is equal to "Y", it begans a while condition
# select = is equal to low, mid and high which are variable which have their own meaning and when the user inputs the variables, they all display something different
# rent = if low is equal to 2 then the rent will now equal 2 and this applies to Low, mid and equal
# itemPrice = price of item that a user inputs
# itemName = name of item that a user inputs
# groceryTotal = total of groceries
# groceryTenderedCash = the amount of money given at the grocery store
# groceryChangeRecieved = the amount of money given back at the grocery store
# letsGO = if this equal why then it will start the while condition in the third partition of this code
# 
#
#
#NOTES: : 
#----------------------------------------------------
#start code below :]
print("\t Welcome to the BitLife Simulator")




totalGross = 0
totalTax = 0
totalNetPay = 0
bankAccountTotal = 0

startGame = "Y"

# Have the user enter their name
# Change to when because if doesnt work
if (startGame == "Y"):
    name = (input("Enter your character's name "))
    name = name.upper()
    print("\t Hiiii,",name)
    
    print("\n")
    print("Nothing is free in this world so... you need to put them hours in!!!")

    jobName = input(" Where do you work? ")
    hoursWK = float(input(" How many hours have you worked "))        
    wage = float(input(" Enter your wage: $ "))
    
    print(" Uncle Sam collects 20%")

    gross = hoursWK * wage
    tax = .2
    tax = tax * gross
    netPay = gross - tax

    print("\n")
    print("\n")
    
    totalGross = totalGross + gross
    totalTax = totalTax + tax
    totalNetPay = totalNetPay + netPay
    print("\t",jobName,"Check")
   

    print(" Total Gross Pay:","$","{0:1.2f}".format(totalGross))
    print(" Total Amount of Taxes:","$","{0:1.2f}".format(totalTax))
    print(" Total Net Pay:","$","{0:1.2f}".format(totalNetPay))

print("\n")
#Create a banking system
bankAccountTotal = totalNetPay
showBAT = "Y"
showBAT= input(" Would you like to see your Checkings Account (Y/N)")
showBAT = showBAT.upper()
if(showBAT == "Y"):
     print(" You current have $ ",bankAccountTotal)
if(showBAT != "Y"):
    print(" WOW")

print("\n")
#Based on your income where can you live ( Low End Apartment, Mid Range Apartment,Condo)
print("Look we all need a place to sleep")
print("\n")        


total = 0
tenderedCash = 0
changeRecieved = 0



low = 50
mid = 100
high = 350

print(" Low End Apartment \t"," Mid Range Apartment \t"," High End Apartment \t")
print(" $ 50 \t"," \t\t\t $ 200 "," \t\t $ 350 ")
print("\n")
print(" Enter 'LOW' for Low End Apt, 'MID' for Mid Range Apt,'HIGH' for High End Apt")

choice = "Y"

while( choice == "Y"):
    select = ["Low","Mid","High"]
    select = input(str("\t\t\tWhich package do you want?"))
    select = select.upper()

    
    
    if(select == "LOW"):
        rent = low
        print("\n")
        print(" Your rent is $","{0:1.2f}".format(rent))
        tenderedCash = float(input(" How much will you give the landlord? $"))
        changedRecieved = tenderedCash - rent
        bankAccountTotal = bankAccountTotal - tenderedCash
        
        print(" Here's your change $","{0:1.2f}".format(changedRecieved))
        print("\n")
        print("\n")
        print(" Onto the next segment of life")
        break
        
    if(select == "MID"):
        rent = mid
        print("\n")
        print(" Your rent is $","{0:1.2f}".format(rent))
        tenderedCash = float(input(" How much will you give the landlord? $"))
        changedRecieved = tenderedCash - rent
        bankAccountTotal = bankAccountTotal - tenderedCash
    
        print(" Here's your change $","{0:1.2f}".format(changedRecieved))
        print("\n")
        print("\n")
        print(" Onto the next segment of life")
        break
        
    if(select == "HIGH"):
        rent = high
        print("\n")
        print(" Your rent is $","{0:1.2f}".format(rent))
        tenderedCash = float(input(" How much will you give the landlord? $"))
        changedRecieved = tenderedCash - rent
        bankAccountTotal = bankAccountTotal - tenderedCash
    
        print(" Here's your change $","{0:1.2f}".format(changedRecieved))
        print("\n")
        print("\n")
        print(" Onto the next segment of life")
        break


print("\n")        
#Create a banking system

showBAT = "Y"
showBAT= input(" Would you like to see your Checkings Account (Y/N)")
showBAT = showBAT.upper()
if(showBAT == "Y"):
    print(" You currently have $ ",bankAccountTotal)
if(showBAT != "Y"):
    print(" WOW")    
    
#make a list just like other project
# Grocery store samething
#In this section you'll notice quite few comments, please disregard them. In the future I plan on coming back to this lab to add name and prices in the same line and have them continue on the next line if the user selects yes to adding another item like so
#       Receipt
#Item Name   Item Price
# water      2.50
# goldfish   5.00
print("\n")
print(" Lets go to the Grocery Store!!!")
print("\n")        



itemPrice = 0
groceryTotal = 0
groceryTotal = groceryTotal + itemPrice
groceryTenderedCash = 0
groceryChangeRecieved = 0

letsGo = "Y"
#numOfItems = 0
#itemNameList = []
#itemPriceList = []

while(letsGo == "Y"):
    itemName = str(input(" What is the name of the item?"))
    #itemNameList.append(itemName)
    
    itemPrice = float(input(" How much is your item? $"))
    #itemPriceList.append(itemPrice)
    
    #print(itemName,itemPrice)
    letsGo = str(input(" Do you want to add more items? (Y/N)"))
    letsGo = letsGo.upper()
    
    groceryTotal = groceryTotal + itemPrice
    
    #dictionary ={"name":[],"price":[]}
    #conversion = list(dictionary.values())
    #name = conversion[0]
    #price = conversion[1]
    #name.append(itemName)
    #price.append(itemPrice)




   
    #numOfItems = numOfItems + 1
    
    if(letsGo != "Y"):
        #print(numOfItems)
        print("\n")   
        #print("Item Name \t"," Item Price \t")
        #print("{0:10}".format(itemNameList))
        #for i in range(len(itemNameList)):
            #print("{0:11}{0:22}".format(itemNameList[i],itemPriceList[i]))
            #print(itemNameList," \t",itemPriceList ,"\t")
        #for i in range(len(name)):
            #print(name[i],price[i])
        #for i in range( min(len(itemNameList), len(itemPriceList)) ):
           #print("{0:10} {0:22}".format(itemNameList[i], itemPriceList[i]))
        #while
            #print("{0:10} {0:22}".format(itemNameList, itemPriceList))
            #print(itemNameList," \t",itemPriceList ,"\t")
        
                
        print("\n")   
        print("\n")
        print(" Your total is $","{0:1.2f}".format(groceryTotal))
        groceryTenderedCash = float(input(" How much will you give the clerk? $"))
        groceryChangedRecieved = groceryTenderedCash - groceryTotal
        bankAccountTotal = bankAccountTotal - groceryTenderedCash 
        print(" Here's your change $","{0:1.2f}".format(groceryChangedRecieved))
        print("\n")
        break
    

# When money is low ask if they want to go back to work below $100
#if(bankAccountTotal > 100):
   # workAgain = input(str("Do you want to work again?... You're a little broke right now. (Y/N) "))
# repeat

print("\n")    
# print an image line by line like in Lab 1 
print(" Thank You for using the BitLife Simulator")

    
    
    





