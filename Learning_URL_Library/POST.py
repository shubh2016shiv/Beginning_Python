'''
Created on Nov 12, 2016

@author: ABC
'''
import urllib.request as req
import urllib

url = 'https://www.pythonprogramming.net'
values = {'q':'basics'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

request = req.Request(url,data)

response = req.urlopen(request)
try:
    res_file = open('read_response.txt','w')
    print("The file is opened!")
    res_file.write(str(response.read()))    
except:
    print("Some error!")
finally:
    res_file.close()
    print("The file is closed!")