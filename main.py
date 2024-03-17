# Description: QAP# 4 - One stop Insruance Company
# Author: Brandon Shea
# Date(s): March 14th 2024 - 

# Define required libraries.
import FormatValues as FV
import datetime
import sys
import time

# Define program constants.
f = open('def.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
ADD_DISCOUNT = float(f.readline())
EXTRA_LIAB_COV = float(f.readline())
GLASS_COV = float(f.readline())
LOANER_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE = float(f.readline())
f.close()


# Define program functions.


# Main program starts here.
while True:

    # Gather user inputs.
    while True:
        # Customer first name
        custFirstName = input("Enter the customers first name: ")
        if custFirstName == "" or custFirstName == " ":
            print("Error - Customer first name cannot be blank.")
        else:
            break

    while True:
        # Customer last name
        custLastName = input("Enter the customers last name: ")
        if custLastName == "" or custLastName == " ":
            print("Error - Customer last name cannot be blank.")
        else:
            break

    while True:
        # Customer address
        custStrAdd = input("Enter the customers street address: ")
        if custStrAdd == "" or custStrAdd == " ":
            print("Error - Customer street address cannot be empty.")
        else:
            break

    while True:
        # Customer city
        custCity = input("Enter the customer city: ")
        if custCity == "" or custCity == " ":
            print("Errror - Customer city cannot be blank.")
        else:
            break

    provLst = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "SK", "NV"] # Province list
    while True:
        # Customer province
        prov = input("Enter the customer province (XX): ")
        if prov == "":
            print("Error - Customer province cannot be blank")
        elif len(prov) != 2:
            print("Error - Must be two characters only")
        elif prov not in provLst:
            print("Error - Invalid Province")
        else:
            break
    # Perform required calculations.

    # Display results
    

# Any housekeeping duties at the end of the program