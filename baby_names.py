import sys
import re

def extract_names(filename):
    """
    Given a file name for a baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ' ...]
    """
    names = []

    # Open and read the file.
    with open(filename, 'rt', encoding='utf-8') as f:
        text = f.read()

    # Extract the year.
    year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not year_match:
        sys.stderr.write('Couldn\'t find the year!\n')
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)

    # Extract all the name and rank tuples.
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

    # Store the names and ranks in a dictionary to ensure no duplicates.
    names_to_rank = {}
    for rank_tuple in tuples:
        rank, boyname, girlname = rank_tuple
        if boyname not in names_to_rank:
            names_to_rank[boyname] = rank
        if girlname not in names_to_rank:
            names_to_rank[girlname] = rank

    # Get the sorted list of names
    sorted_names = sorted(names_to_rank.keys())

    # Build the result list
    for name in sorted_names:
        names.append(name + ' ' + names_to_rank[name])

    return names


def main():
    # Process command-line arguments
    if len(sys.argv) < 2:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    summary = False
    if sys.argv[1] == '--summaryfile':
        summary = True
        del sys.argv[1]

    # For each input file, get the names, then either print the text output
    # or write it to a summary file
    for filename in sys.argv[1:]:
        names = extract_names(filename)

        # Make text out of the whole list
        text = '\n'.join(names)

        if summary:
            # Write the summary to a new file
            with open(filename + '.summary', 'w', encoding='utf-8') as outf:
                outf.write(text + '\n')
        else:
            # Print the summary to stdout
            print(text)


if __name__ == '__main__':
    main()
