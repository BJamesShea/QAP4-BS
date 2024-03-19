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

    while True:
        customerData = FUN.customerInfo()
        insuranceInformation = FUN.vehicleInfo()
        paymentInformation = FUN.paymentInfo()
        claimInformation = FUN.claimInfo()

        numCars, extraLiab, glassCoverage, loanerCar = insuranceInformation
        paymentMethod, downPayment = paymentInformation

        if numCars == 1:
            insurancePremium = BASIC_PREM
        elif numCars > 1:
            insurancePremium = BASIC_PREM * ADD_DISCOUNT

        if extraLiab == "Y":
            extraLiabilityCost = EXTRA_LIAB_COV
        else:
            break

        if glassCoverage == "Y":
            glassCoverageCost = GLASS_COV
        else:
            break

        if loanerCar == "Y":
            loanerCarCost = LOANER_CAR
        else:
            break

        totalExtraCost = extraLiabilityCost + glassCoverageCost + loanerCarCost

        totalInsurancePremium = BASIC_PREM + totalExtraCost

        HST = totalInsurancePremium * HST_RATE

        finalCost = totalInsurancePremium + HST

        if paymentMethod == "Down Payment":
            monthlyPayment = (finalCost - downPayment) + PROC_FEE / 8
        else:
            monthlyPayment = (PROC_FEE + finalCost) / 8


            # Display results



        # Any housekeeping duties at the end of the program