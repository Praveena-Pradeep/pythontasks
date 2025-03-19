import sys
import re

def extract_names(year_to_find):
    """
    Extract names and ranks from baby*.html file corresponding to the given year.
    Returns a list starting with the year, followed by 'name rank' strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    # List to store the result
    names = []
    
    # Read the HTML file for the year
    filename = f'baby{year_to_find}.html'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Could not find the file for the year {year_to_find}. Make sure the file baby{year_to_find}.html exists.")
        sys.exit(1)

    # Extract the year from the HTML (just to make sure it's the correct file)
    year_match = re.search(r'Popularity\sin\s(\d{4})', text)
    if not year_match or year_match.group(1) != year_to_find:
        print(f"Year {year_to_find} not found in the file.")
        sys.exit(1)

    # Add the year to the result
    names.append(year_to_find)

    # Extract all names and ranks (boy and girl names)
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    
    # Create a dictionary to store the names and their ranks
    names_to_rank = {}
    for rank_tuple in tuples:
        rank, boy_name, girl_name = rank_tuple
        # Add the boy and girl names to the dictionary (if not already there)
        if boy_name not in names_to_rank:
            names_to_rank[boy_name] = rank
        if girl_name not in names_to_rank:
            names_to_rank[girl_name] = rank
    
    # Sort the names alphabetically
    sorted_names = sorted(names_to_rank.keys())

    # Add 'name rank' to the result list
    for name in sorted_names:
        names.append(f'{name} {names_to_rank[name]}')

    return names

def main():
    # Ask for the year input
    year_to_find = input("Enter the year you want to search for (e.g., 1990): ").strip()

    # Process command-line arguments
    if len(sys.argv) < 2:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    summary = False
    if sys.argv[1] == '--summaryfile':
        summary = True
        del sys.argv[1]

    # Extract names and ranks for the input year
    names = extract_names(year_to_find)

    # Convert the result list into a string with each name on a new line
    text = '\n'.join(names)

    if summary:
        # Write the result to a summary file
        with open(f'{year_to_find}.summary', 'w', encoding='utf-8') as outf:
            outf.write(text + '\n')
    else:
        # Print the result to the console
        print(text)

if __name__ == '__main__':
    main()
