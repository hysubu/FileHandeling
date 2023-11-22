
'''
remove(): if we want to remove any file we can use this method
'''

import os
# open("file.txt" , "x")

# os.remove("file.txt")


'''
------------------------------ Example : 2 ---------------------------
remove file using exists() method 
'''

path = "file.txt"
if os.path.exists(path):
    os.remove(path)
else:
    print("file doesnot exists ")