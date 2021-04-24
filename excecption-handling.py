#Error examples

#1/0 #ZeroDivisionError occurs when you try to divide by zero.

#y=a+5 #NameError in this case means that you tried to use the variable a when it was not defined.

#a=[1,2,3]
#a[10] #IndexError in this case occurs when you try to access data from a list using an index that does not exist for this list.



##Exception Handling
#Try except

# potential code before try catch

#try:
    # code to try to execute
#except:
    # code to execute if there is an exception
    
# code that will still execute if there is an exception

#Example1
a=1
try:
    a=int(input('Please enter a number to divide a'))
    #a=a/b #for run remove #
    print('Sucess a=',a)
except:
    print('There was an error')
2
10


##Try Except Specific:

# potential code before try catch #
#try:
    # code to try to execute
#except (ZeroDivisionError, NameError):
    # code to execute if there is an exception of the given types
# code that will execute if there is no exception or a one that we are handling


# potential code before try catch #
#try:
    # code to try to execute
#except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
#except NameError:
    # code to execute if there is a NameError   
# code that will execute if there is no exception or a one that we are handling


##Try Except Specific Example

a=1
try:
    b=int(input("Please enter a number to divide a"))
    a=a/b
    print('Success a=',a)
except ZeroDivisionError:
    print('The number you provide cant divide 1 because it is 0')
except ValueError:
    print('You did not provide a number')
except:
    print('Someting went wrong')
0
10
1
'avemaria'



### Try Except Else and Finally


# potential code before try catch
#try:
    # code to try to execute
#except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
#except NameError:
    # code to execute if there is a NameError
#except:
    # code to execute if ther is any exception
#else:
    # code to execute if there is no exception
    
# code that will execute if there is no exception or a one that we are handling

# potential code before try catch

#try:
    # code to try to execute
#except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
#except NameError:
    # code to execute if there is a NameError
#except:
    # code to execute if ther is any exception
#else:
    # code to execute if there is no exception
#finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling


# Try Except Else and Finally Example

a=1
try:
    b=int(input('Please enter a number to divide a'))
    a=a/b
except ZeroDivisionError:
    print('The number you provided cant divide 1 because it is 0')
except ValueError:
    print('You did not provide a number')
except:
    print('Something went wrong')
else:
    print('Sucess a=',a)    

'y'
'00'
0.79

#example2
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")

59