def Append(name):
    file = open(f"{name}" , "a")
    txt = input("Write your text:\n")

    file.write(f"\n{txt}")

def Read(name):
    file = open(f"{name}" , R"r")

    print(file.read())   

def Write(name):
    file = open(f"{name}" , "w")
    txt = input("Write your text:\n")

    file.write(f"{txt}")


file_name = input("Enter name of file: ")

num = int(input("1-read\n2-write\n3-append\n"))

if num == 1:
    try:
        Read(file_name)
    except:
        print("Your name of file is wrong")

elif num == 2:

    try:
        Write(file_name)
    except:
        print("Your name of file is wrong")

elif num == 3:

    try:
        Append(file_name)
    except:
        print("Your name of file is wrong")

else:
    print("There is no such function")




