
# Levi Germeil
# Final Exam
# December 12,2022
# SE116.01
# PROGRAM PROMPT: Write a Python program that will determine the change a user will receive based on the total cost 
# of all items purchased.  Some items might be discounted. All discounted items are 5% off. Some 
# of the items purchased might be taxable. The sales tax for all taxable items is 7%.  The user 
# should be allowed to enter as many items as they want. Before the user enters the price of an 
# item the program should prompt the user to see if the item is discounted. If the user enters d 
# then the item is discounted.  The user should be able to enter a lowercase or uppercase d.
# When the user has finished entering all their items the program should display the total amount 
# of all items (before discounts are applied and before tax), the total amount of the discounted 
# items, the total tax, and the total amount The total amount will be the total of all items minus the 
# discounts then add the tax.  Print out the change the user will receive. All money must be 
# rounded to the nearest cent. The user should be able to enter a lowercase or uppercase y or n 
# when prompted to see if there are any more items.
#
#
#varName        description of data it will hold
# itemPrice = Price of item
# letsGo = " Do you want to add more items?" is the user will be prompted to answer
# total = Sum of all the items
# tenderedCash = " How much money will you give the clerk?"
# changeRecieved = How much change the customer recieves
# isItemTaxable = is the item taxable
# subTotal = subtotal
# totalSalesTax = all the sales tax combined
# salesTax = the itemPrice times .07
# afterDisc = the subtotal of item(s) minus the discount
# discount = the money taken of the item
# totalDiscounts = a sum of all the discounts
#
#NOTES: include any notes you may find useful
#----------------------------------------------------
#start code below :]


itemPrice = 0
totalSalesTax = 0
subTotal = 0
subTotal = subTotal + itemPrice
discount = 0
totalDiscounts = 0
totalDiscounts = totalDiscounts + discount
afterDisc = subTotal - totalDiscounts
total = 0
tenderedCash = 0
changeRecieved = 0
letsGo = "Y"
isItemTaxable = "T"
isItemDisc = "D"


while(letsGo == "Y"):
	
    itemPrice = float(input(" How much is your item? $"))
    ###
    isItemDisc = input(" Is item discounted? If so enter 'D',If not press enter :")
    isItemDisc = isItemDisc.upper()
    if(isItemDisc == "D"):
        discount = itemPrice * .05
    
    ###
    isItemTaxable = str(input(" Is this item taxable? If so enter 'T',If not press enter :"))
    isItemTaxable = isItemTaxable.upper()
    if(isItemTaxable == "T"):
        salesTax = itemPrice * .07
        totalSalesTax = totalSalesTax + salesTax
    ###
    letsGo = str(input(" Do you want to add more items? (Y/N)"))
    letsGo = letsGo.upper()
    totalDiscounts = totalDiscounts + discount
    subTotal = subTotal + itemPrice
    afterDisc = subTotal - totalDiscounts
    total = afterDisc + totalSalesTax
    #Total cost of all items before discount
        #that would be subtotal
    #Total discounts
        #that would be totalDiscounts
    #Total cost of items after discount
        #that would be afterDisc = subTotal - totalDiscounts

#Total cost of all items before discount $15.00
#do some subtraction math ig
#Total discounts
#
#Total cost of items after discount           14.25
      
print("\n")
#Total cost of all items before discount $15.00
print(" Your subtotal is $","{0:1.2f}".format(subTotal))
#Total discounts
print(" Total discounts is $","{0:1.2f}".format(totalDiscounts))
#Total cost of items after discount
print(" Total cost of items after discount is $","{0:1.2f}".format(afterDisc))
#Total tax  
print(" Your total sales tax is $","{0:1.2f}".format(totalSalesTax))
#Please pay this amout  
print(" Your overall total is $","{0:1.2f}".format(total))
tenderedCash = float(input(" How much will you give the clerk? $"))
changedRecieved = tenderedCash - total
print(" Here's your change $","{0:1.2f}".format(changedRecieved))
print("\n")
print("\n")
input(" Press Enter to exit the program")
