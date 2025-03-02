import os 

file_name = input("Write your file name: ")
 
if os.path.exists(file_name):
    os.remove(file_name)
    print("The file is deleted")
else:
    print('The file does not exists')