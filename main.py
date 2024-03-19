# Description: QAP# 4 - One stop Insruance Company
# Author: Brandon Shea
# Date(s): March 14th 2024 - 

# Define required libraries.
import FormatValues as FV
import datetime
import sys
import time
import functions as FUN


while True:
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

    curDate = datetime.datetime.now()

    # Define program functions.

    # Main program starts here.
        
    # Gather user inputs.
    
        # Perform required calculations.
    finalCost = 0
    while True:
        customerData = FUN.customerInfo()
        insuranceInformation = FUN.vehicleInfo()
        paymentInformation = FUN.paymentInfo()
        claimInformation = FUN.claimInfo()

        custFirstName, custLastName, custStrAdd, custCity, prov, postCode, phoneNum   = customerData
        numCars, extraLiab, glassCoverage, loanerCar = insuranceInformation
        paymentMethod, downPayment = paymentInformation

        if numCars == 1:
            insurancePremium = BASIC_PREM
        elif numCars > 1:
            insurancePremium = BASIC_PREM * ADD_DISCOUNT

        if extraLiab == "Y":
            extraLiabilityCost = EXTRA_LIAB_COV
        else:
            extraLiabilityCost = 0

        if glassCoverage == "Y":
            glassCoverageCost = GLASS_COV
        else:
            glassCoverageCost = 0

        if loanerCar == "Y":
            loanerCarCost = LOANER_CAR
        else:
            loanerCarCost = 0

        totalExtraCost = extraLiabilityCost + glassCoverageCost + loanerCarCost

        totalInsurancePremium = BASIC_PREM + totalExtraCost

        HST = totalInsurancePremium * HST_RATE

        finalCost = totalInsurancePremium + HST

        if paymentMethod == "Down Payment":
            monthlyPayment = (finalCost - downPayment) + PROC_FEE / 8
        else:
            monthlyPayment = (PROC_FEE + finalCost) / 8


    


        # DSPs conversions
        customerName = custFirstName + " " + custLastName
        







        # Display results
        print("----------------------------------------------")
        print()
        print("----------------------------------------------")
        print("----------ONE STOP INSURANCE COMPANY----------")
        print("----------------------------------------------")
        print()
        print("             CUSTOMER INFORMATION             ")
        print()
        print("----------------------------------------------")
        print(f"Customer Name:     {customerName:<20s}       ")
        print(f"Address:           {custStrAdd:<20s}         ")
        print(f"City:              {custCity:<14s}           ")
        print(f"Province:          {prov:<2s}                ")
        print(f"Postal Code:       {postCode:<6s}            ")
        print(f"Phone Number:      {phoneNum:<12s}           ")
        print()
        
        
        
        
        
        
        
        
        
        
        
        print(f"{finalCost}")


        # Any housekeeping duties at the end of the program