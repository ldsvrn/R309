#!/usr/bin/env python3

import threading
import time
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

img_urls = [
    "https://images.pexels.com/photos/2559941/pexels-photo-2559941.jpeg",
    "https://images.pexels.com/photos/15286/pexels-photo.jpg",
    "https://images.pexels.com/photos/1624600/pexels-photo-1624600.jpeg",
]


def download_image(img_url):
    logging.info(f"Starting downloading {img_url}")
    img_bytes = requests.get(img_url).content
    img_name = img_url.split("/")[-1]
    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        logging.info(f"{img_name} was downloaded")


def main():
    T = []
    for i, item in enumerate(img_urls):
        T.append(threading.Thread(target=download_image, args=[item]))
        T[i].start()

    for i in T:
        i.join()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    logging.info(f"Tasks ended in {round(end - start, 2)} second(s)")
