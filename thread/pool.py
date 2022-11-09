#!/usr/bin/env python3

import concurrent.futures
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


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end = time.perf_counter()
    logging.info(f"Tasks ended in {round(end - start, 2)} second(s)")
