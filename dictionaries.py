#Create the dicionary
Dict={'key1':1,'key2':'2','key3':[3,3,3],'key4':(4,4,4),'key5':5,(0,1):6}
Dict

#Access to the value by the key
Dict['key1']

#Access a sample dictionary
release_year_dict={'Thriller':'1982','Back in Black':'1980',\
                    'The Dark of the Moon':'1973','The Bodyguard':'1992',\
                    'Bat Out of Hell':'1977','Their Greatest Hits (1971-1975)':'1976',\
                    'Saturday Night Fever':'1977','Rumours':'1977'}
release_year_dict

#Get value by keys
release_year_dict['Thriller']
release_year_dict['The Bodyguard']

#Get all the keys in dictionary
release_year_dict.keys()

#Get all the values in dictionary
release_year_dict.values()

#Append value with key into dictionary
release_year_dict['Graduation']='2007'
release_year_dict

#Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict

#Verify the key is in the dictionary
'The Bodyguard' in release_year_dict

##Quiz on Dictionaries##

#Question sample dictionary
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 

#a)In the dictionary soundtrack_dic what are the keys?
soundtrack_dic.keys()
#b) In the dictionary soundtrack_dic what are the values ?
soundtrack_dic.values()

#c)Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.
album_sales_dict={'Back in Black':'50','The Bodyguard':'50','Thriller':'65'}
album_sales_dict

#d)Use the dictionary to find the total sales of Thriller:
album_sales_dict['Thriller']

#e)Find the names of the albums from the dictionary using the method keys():
album_sales_dict.keys()

#f)Find the values of the recording sales from the dictionary using the method values:
album_sales_dict.values()
