# Levi Germeil
# Lab 7
# December 13,2022
# SE116.01
# PROGRAM PROMPT:  Function Practice 
# Write a program that gives the user the following options: 
#       My Basic Calculator 
#   1. Add two numbers (Addition)
#   2. Subtract two numbers (Subtraction)
#   3. Multiply two numbers (Multiplication
#   4. Divide two numbers (Division)
#   5. Exit 
#
#varName        description of data it will hold
# greetings = just print a welcome message to the user
# leMenu = print a menu of options to the user, ask user for their choice, and return said choice to the main program
# funcSelection = gain the user's choice
# addition = ask the user for two numbers, add them together, and print the result 
# total = the sum of "a1" and "a2"
# a1 = the first number being added
# a2 = the second number being added
# total = addition(a1,a2)
# subtraction = sent two values to have one subtracted from the other and return the result
# remainder = the difference between "sub1" and "sub2"
# remain = subtraction(sub1, sub2)
# division = sent two values to be divided
# quotient = the result of d1 being divided by d2
# quotient = d1 / d2 
# multiplication = sent two values to be multiplied
# product = the result of m1 being multiplied by m2
# product = m1 * m2 
# runProgram = "run"
# selection = Allows the user the select a function from the menu
# selection = leMenu()
#
#
#
#
#
#
#
#
#
#
#
#
#
#NOTES: include any notes you may find useful
#----------------------------------------------------
#start code below :]

def greetings():
    print("\n\t\t~WELCOME TO THE SIMPLE CALCULATOR~\n")

#le menu de function
def leMenu():
    print("\tA.   ADDITION")
    print("\tS.  SUBTRACTION")
    print("\tM. MULTIPLICATION")
    print("\tD.   DIVISION")
    print("\tE.      EXIT")
    funcSelection = input("Enter your choice: ")
    funcSelection = funcSelection.upper()
    return funcSelection

#addition function -- ask the user for two numbers, add them together, and print the result 
def addition(a1,a2):
    print("Addition Function")
    total = a1 + a2
    return total
    

#subtraction function -- sent two values to have one subtracted from the other and return the result
def subtraction(w,x):

  print("subtraction function")

  remainder = w - x

  return remainder
#def subtraction():

  #print("Subtraction Function")

  #s1 = float(input("\t\t Enter first number: "))

  #s2 = float(input("\t\tEnter second number: "))

  #remainder = s1 - s2 

  #print("\n\tThe REMAINDER of {0} - {1} = {2}\n".format(s1, s2, remainder))
#division function -- sent two values to have one subtracted from the other and return the result
def division():

  print("division Function")

  d1 = float(input("\t\t Enter first number: "))

  d2 = float(input("\t\t Enter second number: "))

  quotient = d1 / d2 

  print("\n\tThe QUOTIENT of {0} divided by {1} = {2}\n".format(d1, d2, quotient))

#multiplication function -- sent two values to have one subtracted from the other and return the result
def multiplication():

  print("Multiplication Function")

  m1 = float(input("\t\t Enter first number: "))

  m2 = float(input("\t\t Enter second number: "))

  product =m1 * m2 

  print("\n\tThe PRODUCT of {0} mutliplied by {1} = {2}\n".format(m1, m2, product))

#######################################################################################
runProgram = "run"
greetings()
while(runProgram == "run"):
    selection = leMenu()
    
    if selection == "A": #ADDITION
        print("you have chosen addition!")
        a1 = float(input("\t\t Enter first number: "))
        a2 = float(input("\t\t Enter second number: "))
        total = addition(a1,a2)
        print("\n\tThe SUM of {0} + {1} = {2}\n".format(a1, a2, total))


    elif selection == "S": #SUBTRACTION
        #print("you have chosen subtraction!")
        #subtraction()
########################
        print("you have chosen subtraction")
        sub1 = float(input("\t\t Enter first number: "))
        sub2 = float(input("\t\t Enter second number: "))
        remain = subtraction(sub1, sub2)
        print("\n\tThe DIFFERENCE of {0} - {1} = {2}".format(sub1, sub2, remain))
########################

    elif selection == "M": #MULTIPLICATION
        print("you have chosen multiplication!")
        multiplication()
    elif selection == "D": #DIVISION
        print("you have chosen division!")
        division()
    elif selection == "E": #EXIT
        print("you have chosen to exit!")
        runProgram = "stop"
    else: 
        print("***INVALID ENTRY. PLEASE TRY AGAIN.***")

