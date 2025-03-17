def both_ends(s):
   if len(s) < 2:
     return ""
   else:
     return s[0:2] + s[-2:]
user_input = input("Enter a string:")
result = both_ends(user_input)
print(result)

