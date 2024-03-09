# stores the urls gathered from API into a file
def store_urls(urls: list):
    with open("imageurls.txt", "w") as f:
        for url in urls:
            f.write(url + "\n")


# retrieves the urls from file and returns them
def open_urls():
    try:
        with open("imageurls.txt", "r") as f:
            urls = f.readlines()
            urls = [url.strip() for url in urls]
            return urls
    except FileNotFoundError:
        print("File not found.")
