import sys

def word_count_dict(filename):
    """Returns a word/count dictionary for the given filename."""
    word_count = {}
    with open(filename, encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + 1
    return word_count

def print_words(filename):
    """Prints words and their counts, sorted alphabetically."""
    word_count = word_count_dict(filename)
    for word in sorted(word_count):
        print(word, word_count[word])

def print_top(filename):
    """Prints the top 20 most frequent words and their counts."""
    word_count = word_count_dict(filename)
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words[:20]:
        print(word, count)

def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
    main()
