def fix_start(s):
    first_char = s[0]
    print(f"First character: {first_char}")  # Debugging line
    return first_char + s[1:].replace(first_char, '*')

word = input("Enter the string: ")

result = fix_start(word)
print(f"Result: {result}")  # Debugging line
