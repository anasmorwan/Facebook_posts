import time
from sheets import get_next_item, mark_posted
from drive import download_image
from formatter import format_post
from config import CHECK_INTERVAL


def process_once():
    idx, item = get_next_item()

    if not item:
        print("No items in queue...")
        return

    print("Processing:", item["text"])

    image_path = download_image(item["image_url"])
    post_text = format_post(item["text"], item["price"])

    print(post_text)
    print("Image:", image_path)

    # لاحقًا: النشر هنا

    mark_posted(idx)


def run():
    while True:
        process_once()
        time.sleep(CHECK_INTERVAL)
