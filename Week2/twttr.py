vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

word = input("Input: ")

new_word = ""

for char in word:
    if char not in vowels:
        new_word += char

print("Output: " + new_word)