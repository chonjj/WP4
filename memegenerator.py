import requests
import matplotlib.pyplot as pyplt
import matplotlib.image as mpimg
from io import BytesIO
import fileio
import random


# retrieves API response and converts it into a JSON object, then returns it
def get_memes():
    url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

    headers = {
        "X-RapidAPI-Key": "61896b5e36msh8bf1ee0dbbee817p1f55bajsnb97dd77deed2",
        "X-RapidAPI-Host": "programming-memes-images.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    images = response.json()
    response.close()

    return images


# parses through JSON object and stores only image urls
def parse_memes(data):
    data = get_memes()
    url_list = []

    for item in range(len(data)):
        if "image" in data[item]:
            url_list.append(data[item]["image"])

    fileio.store_urls(url_list)


# visualizes the meme
def display_meme():
    images = fileio.open_urls()
    random_img = random.choice(images)

    response = requests.get(random_img)

    img = mpimg.imread(BytesIO(response.content), format="JPG")
    pyplt.imshow(img)
    pyplt.show()
