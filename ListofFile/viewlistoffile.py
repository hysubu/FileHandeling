
import  os
folder = "E:\GIT\FileHandeling\ListofFile"
files = os.listdir(folder)
print(files)

for file_name in files :
    old_name = os.path.join(folder,file_name)
    new_name = old_name.replace(".txt" , ".pdf")
    os.rename(old_name,new_name)
print("after rename")
print(os.listdir(folder))