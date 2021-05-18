#Writing files in python

#Write line to file
exmp2 = '/home/enatielly/workspace/studying-python/Example2.txt'
with open(exmp2,'w') as writefile:
    writefile.write('This is line A')
    
#REad file
with open(exmp2,'r') as testwritefile:
    print(testwritefile.read())
    
#Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write('This is line A\n')
    writefile.write('This is line B\n')
    
#Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines

#Write the strings in the list to text file
with open('Example2.txt','w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
        
#Verify if writing to file is successfully executed
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
#"w" overwrites all the existing data in the file.
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
#Appending Files

#Write a new line to text file
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write('This is line C\n')
    testwritefile.write('This is line D\n')
    testwritefile.write('This is line E\n')
    
#Verify if the new line is in the text file
with open('Example2.txt','r') as testwritefile:
    print(testwritefile.read())

#Additional modes r+ w+ a+
with open('Example2.txt','a+') as testwritefile:
    testwritefile.write('This is line E\n')
    print(testwritefile.read())
    
#tell() and seek(offset,from)
with open('Example2.txt','a+') as testwritefile:
    print('Initial location: {}'.format(testwritefile.tell()))
    
    data = testwritefile.read()
    if(not data): #empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())
    
    testwritefile.seek(0,0) #Move 0 bytes from beginning
    
    print('\nNew location: {}'.format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)
        
    print('Location after read: {}'.format(testwritefile.tell()))
    
with open('Example2.txt','r+') as testwritefile:
    data = testwritefile.readline()
    testwritefile.seek(0,0) #write at beginning of file
       
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    #testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())


#Copy a File
#Copy file to another
with open('Example2.txt', 'r') as readfile:
    with open('Example3.txt','w') as writefile:
        for line in readfile:
            writefile.write(line)
            
#Verify if the copy is successfully executed
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())            