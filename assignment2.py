#import the three functions from the code_check program to use throughout this program
from  code_check import basicCodeCheck, posititonalCodeCheck, universalPCode
'''
Purpose: The purpose of this program is to allow the user to enter an identification number  and the program 
will return if that code is basic, positional or UPC or none. 
Class: CS1026 002
Professor: Bryan Sarlo 
Author: Sinthuja Jeevarajhan 
'''
#Initiates the lists for basic, positional, universal and for codes that are none of the three
noneList = []
basicCodeList= []
positionalCodeList= []
universalCodeList = []

#Introduce the user to the program, prompt them to enter a code to check
code= input("Hi! Welcome to the identification number check program! Please enter code (digits only) (enter 0 to quit): ")
#Checks if the input equals 0 if the user wishes to exit the program
if code == "0":
    exitCheck = True
else:
    exitCheck = False

#Loop runs if the exit check value 0 is not entered
while not exitCheck:
   #check if the code is a basic code
   basicListCheck= []
   basicListCheck.append(basicCodeCheck(code))
   basicVerify= basicListCheck[0]

   #If the value is a basic code then this statement is outputted to the user
   if basicVerify[0] == True:
        basicCodeList.append(code)
        print(code , "is a valid basic code!")


   #Checks if the code is a positional code
   #Initates the empty positonal list and appends the tested value from code_check
   positionalListCheck = []
   positionalListCheck.append(posititonalCodeCheck(code))
   positionalVerify= positionalListCheck[0]
   #If the value is a positional code
   if positionalVerify[0] == True:
       positionalCodeList.append(code)
       print(code, "is a valid positional code!")

   #Check if the value is a universal code
   universalListCheck = []
   universalListCheck.append(universalPCode(code))
   universalVerify=universalListCheck[0]
   #print(universalVerify)

   #If the code is a universal code this statement is outputted
   if universalVerify[0] == True:
       universalCodeList.append(code)
       print(code, "is a valid universal code!")


   #If the value is none of three types of codes then it appends to the 'none' list
   if basicVerify[0] == False and positionalVerify[0] == False and universalVerify[0]== False:
       noneList.append(code)
       print(code, "is neither basic, positional or a UPC code.")

   #Prompt the user to enter a new value or exit the program if they wish
   code= input("Hi! Welcome to the identification number check program! Please enter code (digits only) (enter 0 to quit): ")
   if code == "0":
        exitCheck = True
   else:
        exitCheck = False

#The following statements are printed to the user once the user enters 0 in the program
#Displays the three types of code lists and the 'none' list
print("Summary: ")
print("Valid Basic Codes: ", basicCodeList)
print("Valid Positional Codes: ", positionalCodeList)
print("Valid Universal Codes: ", universalCodeList)
print("Invalid Codes", noneList)
