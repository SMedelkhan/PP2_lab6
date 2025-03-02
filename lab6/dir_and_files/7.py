file1 = open("A.txt" , "r")
file2 = open("B.txt" , "w")
file2.write(f"{file1.read()}")