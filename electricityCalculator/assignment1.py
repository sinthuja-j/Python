'''
CS 1026 Assignment 1: Home Power Consumption
The purpose of the program is to output the electricity cost for the population using various
mathematical operators.
Author: Sinthuja Jeevarajhan
Sept 21, 2021
'''

#Define the constants for the various rates that can be used
OFF_RATE = 0.085
ON_RATE= 0.176
MID_RATE = 0.119

#Define the constants for the various discounts that can be applied
TOTALU_DISCOUNT = 0.04
ONPEAK_DISCOUNT = 0.05
SENIOR_DISCOUNT = 0.11
discountCheck= False

#Introduce the user to the program and store the input of the energy used during the various peak periods
print("Hi! Welcome to the Electricity Consumption Cost Calculator!")
offP_Hours = float(input("To get started...Please enter your energy consumption during Off Peak Hours (7pm-7am) in kwh: "))
#Provide the user with input and exit the program if the user enters 0 or less for off peak hours

while offP_Hours > 0:
    onP_Hours = float(input("Please enter your energy consumption during On Peak hours (5pm-7pm) or (7am-11am) in kwh: "))
    midP_Hours = float(input("Please enter your energy consumption during Mid Peak hours (11am-5pm): "))
    senior_Input = input("Are you a senior, please enter (Y/N), case does not matter: ")

    #Calculate the net cost of their electricity prior to discounts and taxes
    netHours= offP_Hours+ onP_Hours+ midP_Hours
    netCost = ((offP_Hours * OFF_RATE ) + (onP_Hours *ON_RATE) + (midP_Hours * MID_RATE))

    #Check if the user is elgible for the total usage discount
    if netHours < 400:
        reduction = 0
        reduction= netCost * TOTALU_DISCOUNT
        netCost = netCost - reduction
        discountCheck = True

    #Check and apply on peak discount if user is eligible
    if (discountCheck == False) and (onP_Hours < 150):
        reduction = 0
        reduction = (onP_Hours * ON_RATE) * ONPEAK_DISCOUNT
        netCost = netCost - reduction

    #Check and apply senior discount if user is a senior
    if senior_Input == "y" or senior_Input == "Y":
        reduction = 0
        reduction = netCost * SENIOR_DISCOUNT
        netCost = netCost - reduction

    #apply the 13% tax to the total
    totalCost= float(netCost * 1.13)

    #output the total cost to the user
    print("Electricity Cost: $%.2f" % totalCost)

    #set the off peak hours variable to 0 to refresh the program
    offP_Hours = 0
    #prompt the user to input the off peak hours to restart the program
    offP_Hours = float(input("\nTo get started...Please enter your energy consumption during Off Peak Hours (7pm-7am) in kwh: "))
