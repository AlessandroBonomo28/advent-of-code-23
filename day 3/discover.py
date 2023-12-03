dict = {}
with open('input.txt', 'r') as file:
    for line in file:
        for char in line:
            if not char.isdigit():
                 dict[char] = 1

print(dict)