def all_elements_true(t):
    return all(t)

bool_list = []

size = int(input("Size: "))

for i in range(size):
    boo = input(f"Element {i+1}: ").strip().lower() == "true"
    bool_list.append(boo)

bool_tuple = tuple(bool_list)

print("Tuple:", bool_tuple)
print("All elements are True:", all_elements_true(bool_tuple))
