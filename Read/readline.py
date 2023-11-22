'''
Reading the data from file using readline() method
how to work : The readline showing the line by line data thats why we use readline() method in filehandling
'''


# file = open("file1.txt" , "r")
# file.readline()
# for i in file:
#     print(i)

'''
Output : 
Iam text file

here my conetent

if you want to open my file ypu can use open() function in availale in python

new line --1

new line --2

ne line --3

ne line --4

ne line --5
'''

'''
------------------------- Example : 2 -----------------------------
readlines() :  its read the file and showing the list of data like inside the list per
 eliment is one line 
'''
# with open("file1.txt" , "r") as read_with_readlines :
#     print(read_with_readlines.readlines())

'''
Output : 
[ 
'\n', 'Iam text file\n', 'here my conetent\n', 
'if you want to open my file ypu can use open() function in availale in python\n',
 'new line --1\n', 'new line --2\n', 'ne line --3\n', 'ne line --4\n', 'ne line --5'
 ]
'''


'''
-------------------------- Example: 3 --------------------------------
readlines(8): 
8 : it  means  its return 8 bytes of character or list of items 
'''
# file = open("file1.txt")
# print(file.readlines(8))

'''
Output :
['\n', 'Iam text file\n']
'''

'''

how to know bytes of character or file 
'''
# import  sys
# file = open("file1.txt" , "r")
# s = sys.getsizeof(file)
# print(s)
'''
Output : 208
'''
