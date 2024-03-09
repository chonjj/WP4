import requests
import matplotlib.pyplot as pyplt
import matplotlib.image as mpimg
from io import BytesIO
import fileio
import random


# retrieves JPEGs from API and stores them into a file
def get_memes():
    url = "https://ronreiter-meme-generator.p.rapidapi.com/images"

    headers = {
        "X-RapidAPI-Key": "61896b5e36msh8bf1ee0dbbee817p1f55bajsnb97dd77deed2",
        "X-RapidAPI-Host": "ronreiter-meme-generator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    images = response.json()
    fileio.store_urls(images)
    response.close()


# creates a meme using API and visualizes it
def make_meme(top_text, bot_text):
    images = fileio.open_urls()
    random_img = random.choice(images)

    url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

    querystring = {"top": top_text, "bottom": bot_text, "meme": random_img,
                   "font_size": "50", "font": "Impact"}

    headers = {
        "X-RapidAPI-Key": "61896b5e36msh8bf1ee0dbbee817p1f55bajsnb97dd77deed2",
        "X-RapidAPI-Host": "ronreiter-meme-generator.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    img = mpimg.imread(BytesIO(response.content), format = "JPG")
    pyplt.imshow(img)
    pyplt.show()
