'''
Writeline(): this function insert multiple string or list of string at the same time  and each string added the file
'''
list_of_data = ["asasasasasaa\n" , "asasasaa\n" , 'dddfdfdfd\n', "wewewewe\n"]
file = open("file3.txt" , "w")
file.writelines(list_of_data)

'''
go to inside the file and there added the data  
Output :
 
asasasasasaa
asasasaa
dddfdfdfd
wewewewe
'''