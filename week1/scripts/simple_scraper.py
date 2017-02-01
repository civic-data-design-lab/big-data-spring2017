#! python

import requests
import bs4

# load and get the website
response = requests.get('http://duspviz.mit.edu/_assets/data/sample.html')

# create the soup
soup = bs4.BeautifulSoup(response.text, "html.parser")

# find all the tags with class city or number
data = soup.findAll(attrs={'class':['city','number']})

# print 'data' to console
print(data)

f = open('rat_data.txt','a') # open new file, make sure path to your data file is correct

p = 0 # initial place in array
l = len(data)-1 # length of array minus one

f.write("City, Number\n") #write headers

while p < l: # while place is less than length
    f.write(data[p].string + ", ") # write city and add comma
    p = p + 1 # increment
    f.write(data[p].string + "\n") # write number and line break
    p = p + 1 # increment

f.close() # close file