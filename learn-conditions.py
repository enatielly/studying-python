#Comparison operators#
#Condition Equal
a=5
a==6

#Greater than sign
i=6
i>5

#Greater than sign
i=2
i>5

#Inequality Sing
i=2
i!=6

#Inequality Sing
i=6
i!=6

#Use equality sign to compare the strings
"ACDC" == "Michael Jackson"

#Use Inequality sign to compare the strings
'ACDC'!='Michael Jackson'

#Compare characters
'B'>'A'

#Compare characters
'BA'>'AB'

#Branching
# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

# Else statement example
age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")


# Elif statment example
age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")


# Condition statement example
album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')


# Condition statement example
album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')

#Logical operators
# Condition statement example
#album_year = 1980
album_year = 2000

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")

#album_year = 1980
album_year = 2000

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
else:
    print ("Album released before 1990's")

print("")
print("Do Stuff..")


# Condition statement example
#album_year = 1990
album_year = 1975

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")
#########
album_year = 1985

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


# Condition statement example
album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")


##Quiz on Conditions##

#Write an if statement to determine if an album had a rating greater than 8. Test it using the rating for the album “Back in Black” that had a rating of 8.5. If the statement is true print "This album is Amazing!"
album_rating=8.5
if album_rating>8:
    print("This album is Amazing")


#Write an if-else statement that performs the following. If the rating is larger then eight print “this album is amazing”. If the rating is less than or equal to 8 print “this album is ok”.
album_rating=8.5
if album_rating>8:
    print("This album is Amazing")
else:
    print("this album is ok")


#Write an if statement to determine if an album came out before 1980 or in the years: 1991 or 1993. If the condition is true print out the year the album came out.
released_album=1975
if (released_album < 1980) or (released_album==1991) or (released_album==1993):
    print("This album came out in year %d" %released_album)