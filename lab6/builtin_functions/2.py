#Original code
txt=input()

up_letter = 0
low_letter = 0

for i in txt:
    if type(i) == str:
        letter1 = i
        letter2 = i.lower()

        if letter1 == letter2:
            up_letter+=1
        else:
            low_letter+=1

print(f"low {low_letter}: ")
print(f"up {up_letter}: ")