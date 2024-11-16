# create  a directory 
import os
# os.mkdir('my_folder')

# with open("my_folder/file1.txt",'w') as f:
#     f.write("file 1")
# with open("my_folder/file2.txt",'w') as f:
#     f.write("file 2")
# with open("my_folder/file3.txt",'w') as f:
#     f.write("file 3")
print(os.listdir("my_folder"))
# exists or not 
print(os.path.exists("my_folder"))
# current directory
print(os.getcwd())
# size of folder or file
print(os.path.getsize("my_folder"))