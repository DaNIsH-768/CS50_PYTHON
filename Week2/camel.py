camel_case = input("camelCase: ")
snake_case = ""

for char in camel_case:
    if char.isupper():
        snake_case += "_" + char.casefold()
    else:
        snake_case += char

print("snake_case: " + snake_case)
