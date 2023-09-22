#!/usr/bin/python3
import os
import sys
import random
import string
import pathlib
import requests
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'image/avif,image/webp,*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://wallhaven.cc/',
}

DOWNLOAD_DIR = f"{str(pathlib.Path.home())}/pics/walls"
retry_list = []

def generate_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))


def get_ext(url):
    return os.path.splitext(url)[1]


def download_wallpaper(url):
    global retry_list
    small_url = f"https://.../{url.split('/')[-1]}"
    print(f"[***] Downloading {small_url}")
    with requests.Session() as session: 
        session.keep_alive = True
        res = session.get(url, allow_redirects=True, headers=headers)
        if res.status_code == 200:
            download_path = f"{DOWNLOAD_DIR}/{generate_id()}{get_ext(url)}"
            open(download_path, 'wb').write(res.content)
            print(f"[+++] Downloading done of {small_url}")
        else:
            print(f"[!!!] Failed to download {small_url}. Appended to retry_list")
            retry_list.append(url)


def wallpaper_search_api(query):
    if query == "--random" or query == "-r":
        query_url = "https://wallhaven.cc/api/v1/search?sorting=random"
    elif query == "--top" or query == "-t":
        query_url = "https://wallhaven.cc/api/v1/search?sorting=toplist"
    else:
        query_url = f"https://wallhaven.cc/api/v1/search?q={query}&sorting=random" 
    
    res = requests.get(query_url, headers=headers)
    response = res.json()
    dl_links = []
    for wallpaper in response["data"]:
        dl_links.append(wallpaper["path"])

    return dl_links


def download_unsucces(url):
    res = requests.get(url, allow_redirects=True, headers=headers)
    if res.status_code == 200:
        download_path = f"{DOWNLOAD_DIR}/{generate_id()}{get_ext(url)}"
        open(download_path, 'wb').write(res.content)
        print(f"[+++] Downloading done of {url}")
    else:
        print(f"[!!!] Failed to download {url}.") 


def retry_unsucces():
    global retry_list
    if len(retry_list) == 0:
        print("[***] No need to retry!")
    else:
        print(f"[***] Retrying to download {len(retry_list)} unsuccess downloaded wallpapers")
        for url in retry_list:
            print(url)
            download_unsucces(url)

    retry_list = []


if __name__ == "__main__":
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    if len(sys.argv) < 2:
        print("Usage waldl.py <search_query>")
        quit()


    query = sys.argv[1]
    wallpapers = wallpaper_search_api(query)

    maxtheads=5

    with ThreadPoolExecutor(max_workers=maxtheads) as executor:
        for wallpaper in wallpapers:
            executor.submit(download_wallpaper, wallpaper)

    retry_unsucces()
    print(f"[+++] Download is complete")
