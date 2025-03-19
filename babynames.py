import sys
import re
import os

def extract_names(year_to_find):
    """
    Extract names and ranks from the baby*.html file corresponding to the given year.
    Returns a list starting with the year, followed by 'name rank' strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ...]
    """
    # List to store the result
    names = []
    
    # Construct the filename for the given year
    filename = f'baby{year_to_find}.html'
    
    # Check if the file exists
    if not os.path.exists(filename):
        print(f"Error: Could not find the file for the year {year_to_find}. Make sure the file {filename} exists.")
        sys.exit(1)

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
    # User-friendly messages
    print("Welcome to the Baby Names Extractor!")
    print("This program extracts baby names and their ranks from HTML files based on the year.")
    print("Please ensure you have the 'baby{year}.html' files in the current directory.")

    # Ask for the year input
    year_to_find = input("Enter the year you want to search for (e.g., 1990): ").strip()

    # Validate the year input
    if not year_to_find.isdigit() or len(year_to_find) != 4:
        print("Error: Please enter a valid year (e.g., 1990).")
        sys.exit(1)

    # Extract names and ranks for the input year
    names = extract_names(year_to_find)

    # Convert the result list into a string with each name on a new line
    text = '\n'.join(names)

    # Ask the user if they want to save the result to a file
    save_to_file = input("Do you want to save the results to a summary file? (y/n): ").strip().lower()

    if save_to_file == 'y':
        # Save the results to a summary file
        summary_filename = f'{year_to_find}.summary'
        with open(summary_filename, 'w', encoding='utf-8') as outf:
            outf.write(text + '\n')
        print(f"The results have been saved to {summary_filename}")
    else:
        # Print the results to the console
        print("Here are the results:")
        print(text)

if __name__ == '__main__':
    main()
