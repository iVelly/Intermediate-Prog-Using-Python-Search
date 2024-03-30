#Levi Germeil
#
#Lab 3A
#
# Octuber 24,2022
#
# SE116.01
#
# PROGRAM PROMPT: Write an employee wage program.  This program will be similar to lab 2A, but you will also 
# include a loop and total counters.  This program should ask an employer (the user of the program) to 
# enter an employee’s name, hours worked in a week, and hourly wage.  After this data has been input 
# into the program, print to the user the employee’s name, gross pay for one week, taxes due for one 
# week (use 20%), and this employee’s net pay.  Then, allow the user to enter a new employee’s 
# information by asking if they would like to.  If the user does have another employee to enter, repeat 
# the process above.  When the user decides they no longer have data to enter, print to them the total 
# number of employees entered during the program session and the total gross pay for the week.  Also 
# include the total tax amounts and the total net pay for all employees. 
# All money should be format rounded to the second decimal place and clearly labeled.  All money 
# should have decimals in alignment with one another. 
# Example:
#   EMPLOYEE: Smith
#   Gross Pay $600.00
#   Taxes Due $120.00
#   Net Pay $480.00
#       Would you like to enter another employee’s information? [y/n]: 
#
#
#
#
# 
#
# VARIABLE DICTIONARY:
#
# employeeName = The name of the employee
# employeeChecked = the amount of employee's entered in the program
# wage = the hourly rate an employee
# hoursWK = The amount of hours the employee worked
# maximumHoursWK = The maximum amount of hours that can be worked in a week is 40
# gross = "wage" times "hoursWK" give the amount of money accumulated during that time
# totalGross = The amount of money all the employee accumulated during time
# tax = The amount of money uncle sam takes for the state
# totalTax = the amount of tax charged to all employees
# netPay = The amount of money the employee pockets
# totalNetPay = the amount of money all the employees pocket
#
#
#NOTES: : 
#----------------------------------------------------
#start code below :]
print("\n Welcome to the Payroll Program")
employeesChecked = 0
employeeName = "Y"
maximumHoursWk = 40
totalGross = 0
totalTax = 0
totalNetPay = 0

while(employeeName == "Y"):
    employeeName = (input("Check employee's information? (Y/N): "))
    employeeName = employeeName.upper()
    
    hoursWK = float(input("Enter hours worked by employees: "))
    while(hoursWK >= maximumHoursWk ):
        print("An employee must work for 40 hours or less ")
        hoursWK = float(input("Enter hours worked by employees: "))
            
    wage = float(input("Enter your employee's wage: $ "))
    print("Uncle Sam collects 20%")

    gross = hoursWK * wage
    tax = .2
    tax = tax * gross
    netPay = gross - tax

    print("\n")

    print("Gross Pay:","$","{0:1.2f}".format(gross))
    print("Tax:","$","{0:1.2f}".format(tax))
    print("Net Pay:","$", "{0:1.2f}".format(netPay))

    employeesChecked = employeesChecked + 1
    employeeName = (input("Check employee's information? (Y/N): "))
    employeeName = employeeName.upper()
    
    
    print("Number of employees entered is",employeesChecked)
    print("\n")
    totalGross = totalGross + gross
    totalTax = totalTax + tax
    totalNetPay = totalNetPay + netPay
   

    print("Total Gross Pay:","$","{0:1.2f}".format(totalGross))
    print("Total Amount of Taxes:","$","{0:1.2f}".format(totalTax))
    print("Total Net Pay:","$","{0:1.2f}".format(totalNetPay))



print("\n")    
print("Thank you for using the Payroll Program")
input("Press enter to exit program")


    
    
    




