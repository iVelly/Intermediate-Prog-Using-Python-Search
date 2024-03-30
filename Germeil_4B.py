#Levi Germeil
#
#Lab 4B
#
# Octuber 31,2022
#
# SE116.01
#
# Prompt: Write a program that will determine the change a user will receive based on the total cost of all items 
#purchased. The user should be able to enter as many items as they want. When a user enters an item’s 
#cost, ask them if this item will be taxed. If the item will be taxed, calculate the taxable amount. When the 
#user has finished entering all of their items the program should display: the total number of items 
#purchased, the total cost of all items, the total taxable amount of taxed items, and the final total due (cost
#+ tax). Once all of the values are printed, prompt the user for amount tendered. Re-print out the final total 
#cost of all items, the amount tendered, and the change the user will receive. All monetary values must be 
#formatted to 2 decimal places.
#
#
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
# isItemTaxable = is the item taxable
# subTotal = subtotal
# totalSalesTax = all the sales tax combined
# salesTax = the itemPrice times .07
#
#
#
#
#
#
#
#NOTES: : 
#----------------------------------------------------
#start code below :]

itemPrice = 0
totalSalesTax = 0
subTotal = 0
subTotal = subTotal + itemPrice
total = 0
tenderedCash = 0
changeRecieved = 0
letsGo = "Y"
isItemTaxable = "Y"


while(letsGo == "Y"):

    itemPrice = float(input("How much is your item? $"))
    isItemTaxable = str(input("Is this item taxable? (Y/N)"))
    isItemTaxable = isItemTaxable.upper()
    if(isItemTaxable == "Y"):
        salesTax = itemPrice * .07
        totalSalesTax = totalSalesTax + salesTax
    letsGo = str(input(" Do you want to add more items? (Y/N)"))
    letsGo = letsGo.upper()
    
    subTotal = subTotal + itemPrice
    total = subTotal + totalSalesTax
    
print("\n")
print(" Your subtotal is $","{0:1.2f}".format(subTotal))
print("Your total sales tax is $","{0:1.2f}".format(totalSalesTax))
print(" Your total is $","{0:1.2f}".format(total))
tenderedCash = float(input("How much will you give the clerk? $"))
changedRecieved = tenderedCash - total
print("Here's your change $","{0:1.2f}".format(changedRecieved))
print("\n")
print("Thank you for using the self checkout program")
print("\n")
input("Press Enter to exit the program")
