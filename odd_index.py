input_string = input("Enter string: ")
result_string = ""

for index in range(len(input_string)):
    if index % 2 == 0:
        result_string += input_string[index]

print(result_string)