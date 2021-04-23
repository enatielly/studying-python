#First example
album_ratings = [10.0,8.5,9,9.5,6,8,10.9]
album_ratings.sort()
print(album_ratings)


#Functions blocks begin def followed by the function name and parentheses ().
#There are input parameters or arguments that should be placed within these parentheses.
#You can also define parameters inside these parentheses.
#There is a body within every function that starts with a colon (:) and is indented.
#You can also place documentation before the body.
#The statement return exits a function, optionally passing back a value.


#Function example: Add 1 to a and store as b
def add(a):
    b=a+1
    print(a,'if you add one',b)
    return(b)

#We can obtain help about a function:
help(add)

#We can call the function:
#Call the function add()
add(1)
add(2)
add(49)

#Defone a function for multiple two numbers
def mult(a,b):
    c=a*b
    return(c)
    
result = mult(12,2)
print(result)

#Use mult() multiply two integers
mult(2,3)

#Use mult() multiply two floats
mult(10.10,3.55)

#Use mult() multiply two different type values together
mult(2,' Michael Jackson')

mult(4,'Michael Jackson')

#Remember:
exemplo = ('nome'+'cidade')
exemplo


##Variables

#Function definition
def square(a):
    
    # Local variable b
    b=1
    c=a*a+b
    print(a,'if you square +1',c)
    return(c)
square(5)

#Initializes Global variable
x=3
#makes function call and return function a y
y=square(x)
y

#Directly enter a number as parameter
square(2)

#Define functions, one with return value None and other without return value
def MJ():
    print('Michael Jackson')
MJ()

def MJ1():
    print('Michael Jackson')
    return(None)
MJ1()

print(MJ())
print(MJ1())

#Define the function for combining strings
def con(a,b):
    return(a+b)
con('Estrela','Star')

def con2(a,b,c):
    return(a+b+c)
con2('This',' is', ' Timão e Pumba')


##Functions make things simple##

#Block 1:
#a and b calculation block1
a1=4
b1=5
c1=a1+b1+2*a1*b1-1
if(c1<0):
    c1=0
else:
    c1=5
c1

#Block2
#a and b calculation block2
a2=0
b2=0
c2=a2+b2+2*a2*b2-1
if(c2<0):
    c2=0
else:
    c2=5
c2

#Make a FUNCTION for the calculation above:
def Equation(a,b):
    c=a+b+2*a*b-1
    if(c<0):
        c=0
    else:
        c=5
    return(c)
Equation(9,5)

#Block3
a1=4
b1=5
c1=Equation(a1,b1)
c1

#Block4
a2=0
b2=0
c2=Equation(a2,b2)
c2


#Pre-defined functions:

#Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)

# Use sum() to add every element in a list or tuple together
sum(album_ratings)

# Show the length of the list or tuple
len(album_ratings)

#Using if/else Statements and Loops in Functions
def type_of_album(artist,album,year_released):
    print(artist,album,year_released)
    if year_released>1980:
        return 'Modern'
    else:
        return 'Oldie'
x=type_of_album('Michael Jackson','Thriller', 1980)
print(x)

#Print the list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)
PrintList(['1',1,'the man','abc'])


#Setting default argument values in your custom functions
#Example for setting param with default value

def isGoodRating(rating=4):
    if(rating<7):
        print("This album sucks it's rating is",rating)
    else:
        print("this album is good its rating is",rating)

# Test the value with default value and with input
isGoodRating()
isGoodRating(10)


#Global variables

#Example of global variable
artist='Michael Jackson'
def printer1(artist):
    #internal_var1 = artist
    print(artist,' is an artist')

printer1(artist)

#printer1(internal_var1) #error because name 'internal_var' is not defined

#create global variables from within a function:
artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)


#Scope of a Variable

# Example of global variable:
myFavouriteBand='AC/DC'
def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
print('AC/DC rating is:',getBandRating('AC/DC'))
print("Deep Purple's rating is",getBandRating('Deep Purple'))
print('My favoutire band is:',myFavouriteBand)

# Example of local variable:
def getBandRating2(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating2("AC/DC"))
print("Deep Purple's rating is: ", getBandRating2("Deep Purple"))
print("My favourite band is", myFavouriteBand)

# Example of global variable and local variable with the same name:
myFavouriteBand = "AC/DC"
def getBandRating3(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating3("AC/DC"))
print("Deep Purple's rating is: ",getBandRating3("Deep Purple"))
print("My favourite band is:",myFavouriteBand)


#Collections and Functions

#When the number of arguments are unknown for a function, They can all be packed into a tuple as shown:
def printAll(*args):# All the arguments are 'packed' into args which can be treated like a tuple
    print('Number of arguments:',len(args))
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

#The arguments can also be packed into a dictionary as shown:
def printDictionary(**args):
    for key in args:
        print(key + ':' + args[key])
printDictionary(Country='Canada',Province='Ontario',City='Toronto')

#Functions can be incredibly powerful and versatile:
def addItems2(list):
    list.append('Three')
    list.append('Four')
myList = ['One','Two']
addItems2(myList)
myList
