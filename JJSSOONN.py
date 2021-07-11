'''
Python offers some modules to convert the following mentioned Python Objects into JSON-:
dict
list
tuple
string
int
float
True
False
None
For this we use json.dumps() method by importing json module


Also we can convert the JSON into Python(dict type) object only
For this we use json.loads() method by importing json module
'''

#case1-: Converting json to python

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y=json.loads(x)
print(y["city"])
# the result is a Python dictionary:

#case2-: Converting python to json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y=json.dumps(x,indent=5,sort_keys=True,separators=('-' , '.'))
print(y)

