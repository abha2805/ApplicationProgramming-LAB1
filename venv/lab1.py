'''
Program: Lab1.py
Programmer: Abha Kamble
Date: September 8, 2023

Description:
This python program reads and processes five numeric values, calculates the average and standard deviation of the numeric values,
and then displays the results along with the student information in a well-formatted output.

Input:
First Name (string): The first name of the student.
Last Name (string): The last name of the student.
Humber Student ID (string): The student's unique ID at Humber.
Five Numeric Values (float): Five positive numeric values.

Output:
The program displays the following information:
Student Information (First Name, Last Name, and Student ID).
A header for displaying numeric values.
The numeric values entered.
The average of the numeric values with 2 decimal places.
The standard deviation of the numeric values with 2 decimal places.

Formula Used:
Average = (Sum of all numeric values) / 5
Variance = (Sum of squares of numeric values) / 5 - (Average^2)
Standard Deviation = sqrt(Variance)

Note:
All numbers are positive numbers and may be entered as floating point numbers,with any number of digits after the decimal-point.
Assume that user will enter 5 inputs and all inputs are validinput values.
'''
# Read Student Information
FirstName=input("Enter First Name: ")           # Read the First name of the student.
LastName=input("Enter Last Name: ")             # Read the Last name of the student.
StudentId=input("Enter Humber Student ID: ")    # Read the student's unique Humber ID.

# Read five positive numeric values (Assume that all inputs are validinput values.)
FirstNumber = float(input("Enter First Number : "))     # Read the First value.
SecondNumber = float(input("Enter Second Number : "))   # Read the Second value.
ThirdNumber = float(input("Enter Third Number : "))     # Read the Third value.
FourthNumber = float(input("Enter Fourth Number : "))   # Read the Fourth value.
FifthNumber = float(input("Enter Fifth Number : "))     # Read the Fifth value.

# Calculate the sum of all numbers and sum of their squares
SumOfAllNumbers = FirstNumber + SecondNumber + ThirdNumber + FourthNumber + FifthNumber
SumOfAllSquares = FirstNumber**2 + SecondNumber**2 + ThirdNumber**2 + FourthNumber**2 + FifthNumber**2

# Calculate the average
Average = SumOfAllNumbers / 5

# Calculate the standard deviation
Variance = (SumOfAllSquares / 5) - (Average**2)
StdDeviation = Variance**0.5

# Format student information
DisplayInfo="%130s%10s\n%140s"%(FirstName,LastName,StudentId)

# Format the header for displaying the entered values
DisplayHeader="%20s%20s%20s%20s%20s%20s%20s\n"%("Number 1","Number 2","Number 3","Number4","Number 5","Average","Std. Deviation1")

# Format the entered values
DisplayValue="%20s%20s%20s%20s%20s%20s%20s\n"%(FirstNumber,SecondNumber,ThirdNumber,FourthNumber,FifthNumber,"%.2f"%Average,"%.2f"%StdDeviation)

# Display the output
print('$-'*70 + '\n' + DisplayInfo + '\n' + '-'*140 + '\n' + DisplayHeader + '\n' + DisplayValue + '\n' + '-'*140)
