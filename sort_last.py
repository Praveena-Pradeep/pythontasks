def sort_last(tuples):
    # Sort the list of tuples by the last element of each tuple
    return sorted(tuples, key=lambda x: x[-1])
   #example usage
tuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(sort_last(tuples))
