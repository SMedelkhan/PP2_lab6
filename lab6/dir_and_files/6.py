Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYZ"

for letter in Alphabet:
    file = open(f"{letter}.txt" , "w")
    file.write(f"This file is {letter}.txt")

