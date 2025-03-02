size = int(input("Size if list: "))

lst = []

for i in range(size):
    num = input(f"Element {i+1}: ")
    lst.append(num)

file = open("example.txt" , "a")

my_str ="\n" + str(lst)

file.write(my_str)

