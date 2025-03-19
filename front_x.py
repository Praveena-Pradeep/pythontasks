def front_x(words):
    # Initialize two lists: one for words starting with 'x', 
    # and one for words that don't start with 'x'.
    x_list = []
    other_list = []
    
    # Iterate through each word in the input list
    for w in words:
        # Check if the word starts with 'x'
        if w.startswith('x'):
            x_list.append(w)  # Add to x_list if it starts with 'x'
        else:
            other_list.append(w)  # Add to other_list otherwise
    
    # Return a combined list: first sorted x_list, then sorted other_list
    return sorted(x_list) + sorted(other_list)

# Example usage
words = ["xyz", "yxz", "abc", "xdf", "xmy"]
print(front_x(words))
