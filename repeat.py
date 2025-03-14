def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaims is true, add exclamation marks.
    """

    result = s + s + s
    if exclaim:
        result = result + '!!!'
    return result
print(repeat("Woo Hoo", True)) 
print(repeat("yay", False)) 
