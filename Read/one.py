# How to open file Using File handeling

# Using Open() function to onep the file
# Example:1
# f = open('file1.txt', mode="r")
# r =  Open an existing file for a read operation
# for each in f :
#     print(each)



'''
--------------------------------  Example :2 ------------------------------
Here we using read()  method for read the file data
'''

# fil  = open('file1.txt' , "r")
# print(fil.read())
'''
Output : 
Hi ,
    Iam text file
    here my conetent
    if you want to open my file ypu can use open() function in availale in python
'''




'''
----------------------------------  Example : 3----------------------------
Read the file character wise m
mean  if we wnat to read any number of character so we can use this method 
'''

# file = open("file1.txt" , "r")
# print(file.read(40))

'''
Output: 
Hi ,
    Iam text file
    here my conet

'''



'''
------------------------------------Example:4 ---------------------------------------
Using with statement to read any file data 
'''
# with open("file1.txt", "r") as read_file :
#     data= read_file.read()
# print(data)


'''
Output:
Hi ,
    Iam text file
    here my conetent
    if you want to open my file ypu can use open() function in availale in python
'''

'''
------------------------------- Example : 5 ----------------------------
We can split the line while reading any files in python  using split() method 
'''

# file = open("file1.txt" , "r")
# data= file.read()
# for line in data :
#     word = line.split()
#     print(word)
'''
Output: 
['I']
['a']
['m']
[]
['t']
'''






