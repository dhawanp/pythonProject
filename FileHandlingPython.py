'''
File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist. Will overwrite the existing file

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
'''

f=open("C:\\Users\\windows\\Desktop\\1.txt","a")
f.write("Now the file has more contents")
f=open("C:\\Users\\windows\\Desktop\\1.txt")
print(f.read())

#To read only parts of the file use the following example-:

# print(f.read(12))


#To read only single line of the file use readline(). You can use readline() as many times as you want , in-order to read those particular number of lines
# print(f.readline())


# Close Files
# It is a good practice to always close the file when you are done with it. Use close() to do so

'''
Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:

Example
Remove the file "demofile.txt":

import os
os.remove("demofile.txt")
Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:

Example
Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
Delete Folder
To delete an entire folder, use the os.rmdir() method:

Example
Remove the folder "myfolder":

import os
os.rmdir("myfolder")
Note: You can only remove empty folders.
'''