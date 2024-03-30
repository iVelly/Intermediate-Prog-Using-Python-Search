#Levi Germeil
#
#Lab 3A
#
# Octuber 24,2022
#
# SE116.01
#
#Write a program that will determine the change a user will receive based on the total cost of all 
#items purchased.  The user should be allowed to enter as many items as they want. When the 
#user has finished entering all of their items the program should display the total amount then 
#prompt the user for amount tendered.  Print out the total cost of all items, amount tendered and 
#the change the user will receive. The total and change must be formatted to 2 decimal places.
#
#
#
# 
#
# VARIABLE DICTIONARY:
# itemPrice = Price of item
# letsGo = " Do you want to add more items?" is the user will be prompted to answer
# total = Sum of all the items
# tenderedCash = " How much money will you give the clerk?"
# changeRecieved = How much change the customer recieves
#
#
#
#NOTES: : 
#----------------------------------------------------
#start code below :]

itemPrice = 0
total = 0
total = total + itemPrice
tenderedCash = 0
changeRecieved = 0
letsGo = "Y"


while(letsGo == "Y"):

    itemPrice = float(input("How much is your item? $"))
    letsGo = str(input(" Do you want to add more items? (Y/N)"))
    letsGo = letsGo.upper()
    
    total = total + itemPrice
print("\n")
print(" Your total is $","{0:1.2f}".format(total))
tenderedCash = float(input("How much will you give the clerk? $"))
changedRecieved = tenderedCash - total
print("Here's your change $","{0:1.2f}".format(changedRecieved))
print("\n")
print("Thank you for using the self checkout program")
print("\n")
input("Press Enter to exit the program")



    
    




    
