'''
Created on Nov 12, 2016

@author: ABC
'''
'''Regular expressions are used for 
1. Search for specific string in large amount of data
2. Verify that a string has proper format
3. Find a string and replace it with another string
4. Format data into the proper form for importing 
'''

import re

data = "The ape was at the aperture"

if re.search('ape',data):
    print("There is an ape!")

allApes = re.findall('ape.',data) #Notice the dot after ape
#print(allApes)
for i in allApes:
    print(i)
x=re.finditer('ape.',data)
for i in x:
    print(i) #i contains both span and match
    data_tuple = i.span()
    print(data_tuple)
    print(data[data_tuple[0]:data_tuple[1]])
Str = "Cat mat rat pat"
for i in re.findall('[Cmrp]at',Str):
    print(i)
print('******************************')
for i in re.findall('[c-mC-M]at',Str):
    print(i)
    
''' Substituting the set of strings'''
x = re.compile('[Cm]at')
print(x.sub("Hello",Str)) 
Str = "Cat mat rat pat"       
x = re.compile('[^Cm]at')
print(x.sub("Hello",Str)) 
Str = '''This is a long String
That goes for 
many lines'''
print(Str)
x = re.compile('\n')
print(x.sub(" ",Str))

'''using \d
\d is same as [0-9]
\D is same as [^0-9] '''

Str = "12345... Make some noise!"
print('Matches: ' +  str(len(re.findall("\d",Str))) )
print('Matches: ' +  str(len(re.findall("\d{2,4}",Str))) )

''' Overall Nice Example! '''
exampleStr = '''Shubham is 22 years old,
 Shivang is 17 years old'''
names = re.findall('[A-Z][a-z]*',exampleStr, flags=0)
print(names)
ages = re.findall('\d{2}', exampleStr, flags=0)
print(ages)
dict_names = {}
y=0
for eachname in names:
    dict_names[eachname] = ages[y]
    y+=1
print('Extracted names and ages: '+ str(dict_names))