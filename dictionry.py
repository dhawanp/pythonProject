# '''
# DICTIONARY are MUTABLE
#
# is of form key:value , for example-:
# dict1={key1:value1,key2:value2,key3:value3}
# '''
# dict1={'name':'PRATEEK','age':27,'birth place':'DELHI','country':'INDIA','EMP NO':51807453}
# print(type(dict1))
# print(dict1)
#
'''
# To Access Elements of A Dictionary we have two ways-:
# 1.). Accessing all the Elements of Dictionary
# 2.). Accessing a specific element from the Dictionary ,via-:
# a.). get method and
# b.).via printing a single key required in []
'''
# print(dict1['name'] , dict1['age'])
#
#
# a=dict1.get('name')
# print(a)
# b=dict1.get('nomnom') #Particularly see the O/P here of a non-existent element(O/P==None)
# print(b)
# print(dict1['popcorn']) #KeyError: 'popcorn' an error is generated as we are trying to access a non-existent element

dict2={'name':'PRATEEK','age':27,'birth place':'DELHI','country':'INDIA','EMP NO':51807453}
print(dict2.get('name'))
print(dict2.get('birth place'))
print(dict2.items())
print(dict2.keys())
print(dict2.values())
dict2["pan_card_number"]='abcdefg123456789'
print(dict2)
dict2.update({"key":"value"})
print(dict2)
dict2.pop("key")
print(dict2)
del dict2["pan_card_number"]
print(dict2)