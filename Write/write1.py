'''

Write the data in file using python
using write method
if we want to arite any data in existing file  the data will overriden mean
the old data replace to new data
'''

file = open("file.txt" , "w")
file.write("Hello Iam write file and iam also existing file ")
file.write("Hello Iam write file and iam also existing file2 ")

file.close()



'''
-------------------------------- Example : 2 ---------------------------------
We can write using with() statement 
'''
data = "aaa abaab usdisdsniusds sjdjsdjs sdkjsdjsj ksdjskdj ksdjskdj kjsjsjd wuuwwuueowe oweuwuewenoieiw" \
       "wewieuwiuewuewueuwuie wuewuewiue iuweuwiuewu jhwehwe"
with open("file2.txt" , "w") as write_file :
    write_file.write(data)

