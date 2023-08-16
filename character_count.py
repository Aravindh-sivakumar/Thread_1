input_string = input("Enter the string: ")
character_counts = {}

for char in input_string:
    if char in character_counts:
        character_counts[char] += 1
    else:
        character_counts[char] = 1

result = [{char: count} for char, count in character_counts.items()]
print(result)