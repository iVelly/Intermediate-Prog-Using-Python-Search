#Levi Germeil
#Lab 1B
# Octuber 17,2022
# SE116.01
#PROGRAM PROMPT: You want to develop a program that gathers the user’s hourly pay (use $14.50), hours worked (32/week), 
#and tax rate for a two-week period. Once you have this informa5on, you want to display the user’s Gross 
#Pay, Uncle Sam’s Share (the amount to be removed for taxes), and the User’s Net Pay. All calcula5ons should 
#be limited to run once, rather than numerous 5mes. Include in your flowchart the use of variables and print 
#statements. Use 20% for the tax rate. 
#VARIABLE DICTIONARY:
#wage        The amount the employee gets paid
#hoursWK     The amount of hours worked
#tax         the amount of taxes the employee will pay
#gross       The wage multiplied by hours 
#taxAmount   The gross multiplied by taxes
#netPay      The amount the employee will be left
#
#
#varName        description of data it will hold
#NOTES: include any notes you may find useful
#----------------------------------------------------
#start code below :]

wage = 14.50
hoursWK = 32
tax = 0.2
gross = (wage * hoursWK)* 2
taxAmount = (gross * tax)
netPay = gross - taxAmount
print()
print("You owe uncle sam","$","{0:1.2f}".format(taxAmount))
print("Here's your net pay",netPay)
print ("Adios")
