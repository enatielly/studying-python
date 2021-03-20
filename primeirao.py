#try your first Python output
print("Hello world")

#For clear all terminal#
#import os
#clear = lambda: os.system('cls')
#clear()
#For clear all terminal#

#Types of objects in Python
#Integer
11
#Float
2.14
#String
"Hello, Python 101!"

#Type of 12
type(12)

#Type of 2.14
type(2.14)

#Type of "Hello, Python 101!"
type("Hello, Python 101!")

#Print the type of -1
type(-1)

#Print type of 4
type(4)

#Print type of 0
type(0)

#Print type of 1.0
type(1.0)

#Print type of 0.5
type(0.5)

#Print type of 0.56
type(0.56)

#System settings about float type
import sys
#except ImportError: #tratamento do erro com exceção
    #pass
print(sys.version)


#Verify that this ir an integer
type(2)

#Convert 2 to a float
float(2)

#Convert integer 2 to a float and checj its type
type(float(2))

#Casting 1.1 to integer will result in loss of information
int(1.1)

#Convert a string into an integer
int('1')
type(int('1'))

#Convert a string into an integer with error
int('1 or 2 people')

#Convert the string "1.2" into a float
float('1.2')

#Convert an integer to a string
str(1)
type(str(1))

#Convert a float to a string
str(1.2)
type(str(1.2))

#Value true
True

#Value true without uppercase T
#true #true is not defined

#Value false
False

#Type of True
type(True)

#Type of False
type(False)

#Convert True to int
int(True)

#Convert 1 to boolean
bool(1)

#Convert 0 to boolean
bool(0)

#Convert True to float
float(True)

#EXPRESSIONS

#Addition operation expression
43 + 60 + 16 + 41

#Subtraction operation expression
50 - 60

#Multiplication operation expression
5*5

#Division operation expression
25/5

#Division operation expression
25/6

#Division operation expression with doble // >> the result is rounded to the nearest integer
25//5

#Mathematical expression
30 + 2 * 60

#Mathematical expressiom
(30 + 2) * 60

#Store value into variable
x = 43 + 60 + 16 + 41

#Print out the value in variable
x

#Use another variable to store the result of the operation between variable and value
y = x / 60
y

#Overwrite variable with new value
x = x / 60
x

#Name the variables meaningfully
total_min = 43 + 42 + 57 #Total length of albums in minutes
total_min

#Name the variables meaningfully
total_hours = total_min / 60 #Total length pf albums in hours
total_hours

#Complicate expression
total_hours = (43 + 42 + 57) / 60 #Total hours in a single expression
total_hours

