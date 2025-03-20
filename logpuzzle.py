import re
import os
import sys
import urllib.request
import zipfile

def read_urls(filename):
    # Extract domain from filename
    domain = filename.split('_')[1]
    urls = set()
    
    # Open the log file and extract puzzle URLs
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r'GET (\S*puzzle\S*) HTTP', line)
            if match:
                path = match.group(1)
                full_url = f'http://{domain}{path}'
                urls.add(full_url)
    
    # Return the sorted list of unique URLs
    return sorted(list(urls))

def download_images(urls, dir):
    # Create the directory if it doesn't exist
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    # Download each image from the URL
    for i, url in enumerate(urls):
        print(f"Retrieving {url}...")
        filename = os.path.join(dir, f"img{i}")
        urllib.request.urlretrieve(url, filename)
    
    # Create the index.html file to display the images
    with open(os.path.join(dir, "index.html"), 'w') as index_file:
        index_file.write("<html>\n<body>\n")
        for i in range(len(urls)):
            index_file.write(f'<img src="img{i}">')
        index_file.write("\n</body>\n</html>")

def custom_sort(urls):
    # Sorting function for special pattern
    def sort_key(url):
        match = re.search(r'-(\w+)-(\w+)\.jpg$', url)
        if match:
            return match.group(2)  # Sorting by the second part of the filename
        return url  # Regular sort for other URLs
    
    return sorted(urls, key=sort_key)

def zip_images(directory, zip_filename):
    # Zip the images and index.html into a single zip file
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file), file)

def main():
    if len(sys.argv) < 2:
        print("Usage: python logpuzzle.py <logfile> [--todir <dir>] [--tozip <zipfile>]")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    # Read and sort URLs
    urls = read_urls(filename)
    urls = custom_sort(urls)
    
    # Download images if --todir argument is provided
    if '--todir' in sys.argv:
        dir = sys.argv[sys.argv.index('--todir') + 1]
        download_images(urls, dir)

    # Zip the images if --tozip argument is provided
    if '--tozip' in sys.argv:
        zipfile_name = sys.argv[sys.argv.index('--tozip') + 1]
        zip_images(dir, zipfile_name)

if __name__ == "__main__":
    main()

