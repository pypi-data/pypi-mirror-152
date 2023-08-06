# BMI Calculator
Python BMI Calculator calculates BMI, BMI Category and Health risk from Height and Weight of the persons and total number of overweight people in data.


# Objective :
1. Read the JSON raw data and created new fields for BMI, BMI Category and Health risk.
2. Find out the total number of overweight pesons in data.
3. Validation test case has been performed.

# Prerequisites:
1. BMI Calculator package
2. Python Libraries needed : pandas, json

# Installation:
pip install BMI_Calculator

# Usage :

>> import myhealth
>> 
>> a = myhealth.health("data.json")    # read raw json data
>> 
>> a.getData()           # displays updated dataframe with new columns
>> 
>> a.overweights()       # returns number of over persons

# PyPi Package :
The package has been build and uploaded at https://github.com/manishgupta-ind/code-20220528-manishgupta
