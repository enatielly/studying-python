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
    print(testwritefile.read()
          

#Exercise
#Run this prior to starting the exercise
#from random import randint as rnd

#memReg = 'members.txt'
#exReg = 'inactive.txt'
#fee =('yes','no')

#def genFiles(current,old):
    #with open(current,'w+') as writefile: 
     #   writefile.write('Membership No  Date Joined  Active  \n')
      #  data = "{:^13}  {:<11}  {:<6}\n"
#
 #       for rowno in range(20):
  #          date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
   #         writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


    #with open(old,'w+') as writefile: 
     #   writefile.write('Membership No  Date Joined  Active  \n')
      #  data = "{:^13}  {:<11}  {:<6}\n"
       # for rowno in range(3):
        #    date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
         #   writefile.write(data.format(rnd(10000,99999),date,fee[1]))


#genFiles(memReg,exReg)


#def cleanFiles(currentMem,exMem):
 #   '''
  #  currentMem: File containing list of current members
   # exMem: File containing list of old members
    
    #Removes all rows from currentMem containing 'no' and appends them to exMem
    #'''
    
    #pass 


# Code to help you see the files
# Leave as is
#memReg = 'members.txt'
#exReg = 'inactive.txt'
#cleanFiles(memReg,exReg)


#headers = "Membership No  Date Joined  Active  \n"
#with open(memReg,'r') as readFile:
 #   print("Active Members: \n\n")
  #  print(readFile.read())
    
#with open(exReg,'r') as readFile:
 #   print("Inactive Members: \n\n")
  #  print(readFile.read())

#def cleanFiles(currentMem,exMem):
 #   with open(currentMem,'r+') as writeFile: 
  #      with open(exMem,'a+') as appendFile:
            #get the data
   #         writeFile.seek(0)
    #        members = writeFile.readlines()
            #remove header
     #       header = members[0]
      #      members.pop(0)
                
            #inactive = [member for member in members if ('no' in member)]
            #'''
            #The above is the same as 

            #for member in active:
            #if 'no' in member:
            #    inactive.append(member)
            #'''
            #go to the beginning of the write file
            #writeFile.seek(0) 
            #writeFile.write(header)
            #for member in members:
             #   if (member in inactive):
              #      appendFile.write(member)
               # else:
                #    writeFile.write(member)      
            #writeFile.truncate()
                
#memReg = 'members.txt'
#exReg = 'inactive.txt'
#cleanFiles(memReg,exReg)

# code to help you see the files

#headers = "Membership No  Date Joined  Active  \n"

#with open(memReg,'r') as readFile:
 #   print("Active Members: \n\n")
  #  print(readFile.read())
    
#with open(exReg,'r') as readFile:
 #   print("Inactive Members: \n\n")
  #  print(readFile.read())
