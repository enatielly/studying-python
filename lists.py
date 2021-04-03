#LISTS

#Create a list
L=["Michael Jackson", 10.1, 1982]
L

#Print the elements on each index
print("the same element using negative and positive indexing: \n Positive:", L[0], "\n Negative:", L[-3])
print("the same element using negative and positive indexing: \n Positive:", L[1], "\n Negative:", L[-2])
print("the same element using negative and positive indexing: \n Positive:", L[2], "\n Negative:", L[-1])


#List Content
#Sample List
["Michael Jackson",10.1,1982,[1,2], ("A", 1)]

#List Operations
#Sample list
L = ["Michael Jackson", 10.1, 1982, "MJ", 1]
L

#List slicing
L[3:5]

#Use extend to add elements to list
L = ["Michael Jackson",10.2]
L.extend(["pop",10])
L

#Use append to add elements to list
L=['Michael Jackson',10.2]
L.append(['pop',10]) #If we apply append instead of extend, we add one element to the list
L

#Change the element based on the index
A=['disco',10,1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

#Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:',A)

#Split the string, default is by space
'hard rock'.split()

#Split the string by comma
'A,B,C,D'.split(',')


#Copy and clone list
#Copy (copy by reference) the list A
A=['hard rock',10,1.2]
B=A
print('A:',A)
print('B:',B)

#Examine the copy by reference
print('B[0]:',B[0])
A[0] = 'BANANA'
print('B[0]:',B[0])

#Clone (clone by value) the list A
B=A[:]
B
#Now if you change A,B will not change
print('B[0]:',B[0])
A[0]='Hard rock'
print('B[0]:',B[0])

#Quiz on List#
#Create a list a_list, with the following elements 1, hello, [1,2,3] and True.
a_list = [1,'hello',[1,2,3],True]
a_list

#Find the value stored at index 1 of a_list.
a_list[1]

#Retrieve the elements stored at index 1, 2 and 3 of a_list.
a_list[1:4]

#Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:
A=[1,'a']
A
B=[2,1,'d']
B
A.extend(B) # Can be use A+B
A

E = [1]
E.append([2,3,4,5])
E

J=((1),[2,3],[4])
J[2]

F=((11,12),[21,22])
F[0][1]

'1,2,3,4'.split(',') 

len(("disco",10))