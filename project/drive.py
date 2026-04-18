import requests
from config import IMAGE_FOLDER
import os


def download_image(url, filename="image.jpg"):
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)

    path = os.path.join(IMAGE_FOLDER, filename)

    r = requests.get(url)
    with open(path, "wb") as f:
        f.write(r.content)

    return path
