#Use quotation marks for definig string
"Michael Jackson"

#Use single quatation marks for definig string
'Michael Jackson'

#Digital and spaces in string
'1 2 3 4 5 6'

#Special characters in string
'@#2_#$#@&*'

#Print the string
print("Hello!!")

#Assing string to variable
name="Michael Jackson"
name #Para que a variavel funcione precisa executar antes ou em conjunto o valor da variavel


#INDEXING
#Because indexing starts at 0, it means the first index is on the index 0

#Print the first element in the string
print(name[0])

#Print the element on index 6 in the string
print(name[6])

#Print the element on the 13th index in the string
print(name[13])


#NEGATIVE INDEXING

#Print the last element in the string
print(name[-1])

#Print the first element in the string
print(name[-15])

#Find the length of string
len("Michael Jackson")


#SLICING
#When taking the slice, the first number means the index (start at 0),
#and the second number means the length from the index to the last element you want (start at 1)

#Take the slice on variable name with only index 0 to index 3
name[0:4]

#Take the slice on variable name with only index 8 to index 11
name[8:12]


#STRIDE

#Get every second element. The elements on index 1,3,5...
name[::2]

#Get every second element in the range from index 0 to index 4
name[0:5:2]


#CONCATENATE STRINGS

#Concatenate two strings
statement = name + " is the best"
statement

#Print the string for 3 times
3 * " Michael Jackson"

#Concatenate strings
name = " Michael Jackson"
name = name + " is the best"
name


#ESCAPE SEQUENCES

#New line escape sequence
print(" Michael Jackson \n is the best")

#Tab escape sequence
print(" Michael Jackson \t is the best")

#Include back slash in string
print(" Michael Jackson \\ is the best")

# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best")


#STRING OPERATIONS

#Convert all characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper() # .upper is the method
print("After upper:", b)

c="enatielly rosane goes"
d=c.upper()
print(d)

#Repleace the old substring with the new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace("Michael","Janet") # .repleace is the method
b

#Find the substring in the string.
#Only the index of the first element of substring will be the output
name = "Michael Jackson"
name.find("el") # .find is the method

#Find the substring in the string
name.find("Jack")

# If cannot find the substring in the string
name.find('Jasdfasdasdf')


###QUIZ ON STRINGS###

#What is the value of the variable a after the following code is executed?
a = "1"
a

#What is the value of the variable b after the following code is executed?
b = "2"
b

#What is the value of the variable c after the following code is executed?
c=a+b
c

#Consider the variable d use slicing to print out the first three elements:
d = "ABCDEFG"
d[0:3]

#Use a stride value of 2 to print out every second character of the string e:
e = 'clocrkr1e1c1t'
e[::2]

#Print out a backslash:
print("\\")
print(r"\ ")

#Convert the variable f to uppercase:
f = "You are wrong"
f.upper()

#Consider the variable g, and find the first index of the sub-string snow:

g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.find("snow")

#In the variable g, replace the sub-string Mary with Bob:
g.replace ("Mary", "Bob")

