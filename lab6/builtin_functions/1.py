lst = []


size = int(input("Enter the size of list: "))

for i in range(size):
    num = int(input(f"Number {i+1}: "))
    lst.append(num)

number = 1

def multiplying(number):
    for num in lst:
       number *= num

    return number


print(multiplying(number))