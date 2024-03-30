#Levi Germeil
#
# Lab 4A

#
# Octuber 31,2022
#
# SE116.01
#
# PROGRAM PROMPT: Billy has $100 in the bank. He decides to save $80 a month for 30 years at an interest rate of 5%. How 
#much money will he have in the bank at the end of 30 years if the money is compounded monthly? 
#Build a Python program that Billy can use to enter his savings information and simulate his total 
#savings after the amount of time given.
#
#
#
##
#
#
#
# Variables Used:
#
#   countMonths is the count the amount of months 
#   monthlyDep the amount of money being deposited
#   intRate The percentage of interest
#   months the amount of years times 12 months
#   years the amount of years the user enters
#   monthlyInt calculations for monthly interest
#   monthlyEndBalance calculations for the end of the month balance
#   begBalance calculations for the beginning of the month
#
#
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



#######################################################

countMonths = 0
                
begBalance = float(input(" How much money do you own $"))

monthlyDep = float(input(" Enter Montly Deposit: $"))


intRate = float(input(" Enter Interest Rate i.e.'9% enter 9':"))

years = float(input(" Enter number of years:"))

months =  years * 12
                
intRate = intRate / 100

monthlyInt =  begBalance * intRate / 12

print("Beginning Balance \t"," Interest Accued \t","Monthly End Balance \t")

while(countMonths <= months):
    
    monthlyInt =  begBalance * intRate / 12
    monthlyEndBalance =  begBalance + monthlyInt + monthlyDep
    begBalance = monthlyEndBalance
    countMonths = countMonths + 1
    
    print("{0:10.2f}".format(begBalance),"{0:20.2f}".format(monthlyInt),"{0:30.2f}".format(monthlyEndBalance))
   
    




