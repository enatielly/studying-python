#Use the range
range(3)

#For Loop example

dates=[1982,1980,1973]
N=len(dates)

for i in range (N):
    print(dates[i])

#Example of for loop

for i in range (0,8):
    print(i)

#Example of for loop, loop through list

for year in dates:
    print(year)

#Use for loop to change the elements in list

squares = ['red','yellow','green','purple','blue']

for i in range(0, 5):
    print('Before square', i, 'is', squares[i])
    squares[i] = 'white'
    print('After square', i, 'is', squares[i])


#Loop through the list and iterate on both index and element value
squares=['red','yellow','green','purple','blue']

for i, square in enumerate (squares) :
    print(i, square)



#While loop Example

dates=[1982,1980,1973,2000]
i=0
year=dates[0]
while(year != 1973):
    print(year)
    i = i+1
    year=dates[i]
print('It took',i, 'repetitions to get out of loop.')

#Write a for loop the prints out all the element between -5 and 5 using the range function.
for i in range (-5,6):
    print(i)

#Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

#Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)

#Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
Rating=PlayListRatings[0]
while(Rating>=6):
    print(Rating)
    i=i+1
    Rating=PlayListRatings[i]
print('It took',i, 'repetitions to get out of loop.')

##or

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1

#Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

