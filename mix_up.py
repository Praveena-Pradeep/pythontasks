def mix_up(a, b):
   a_swapped = b[:2]+a[2:]
   b_swapped = a[:2]+b[2:]
   return a_swapped + ' ' + b_swapped

a = input("Enter the first string swap:")
b = input("Enter the second string to swap:")
result = mix_up(a,b)
print(result)
