my_str = input("Write your string: ")

check = True

for i in range(len(my_str)):
    if my_str[i]!=my_str[len(my_str)-1-i]:
        check = False
        break

if check:
    print("palindrome")
else:
    print("Not palindrome")