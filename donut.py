count  = int(input("Enter the number:"))
def donuts(count):

    if count<10:
        return 'Number of donuts:' +str(count)
    else:
       return 'Number of donuts:many'
result = donuts(count)
print(result)
