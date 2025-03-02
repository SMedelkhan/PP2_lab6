direction = input("Enter direction of file: ").strip()

try:
    with open(direction, "r") as file:  # Используем `with open`
        print(file.read())

except FileNotFoundError:
    print("File not found. Check the path.")

except Exception as e:
    print(f"Error: {e}")  
