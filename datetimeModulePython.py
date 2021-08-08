import datetime
x=datetime.datetime.now()
print(x)
'''
It prints the date time in the format of YYYY-MM-DD HH:MM:SS.MICROSECONDS
'''
print(x.day)
print(x.month)
print(x.year)

'''
Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.
'''
#We can also create a date with datetime() class(constructor) of the datetime module
x=datetime.datetime(2021,12,7,15,16,21)
print(x)

'''
The strftime() Method
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
'''
x=datetime.datetime(2021,7,12)
print(x.strftime("%a"))