import requests
from bs4 import BeautifulSoup
import re

URL = "https://catalog.ngc.nvidia.com/containers?filters=nvidia_nim%7CNVIDIA+NIM%7Cnimmcro_nvidia_nim&orderBy=weightPopularDESC"

def fetch_container_count():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find text containing "Displaying"
    displaying_text = soup.find(string=re.compile(r"Displaying \d+ containers"))

    if displaying_text:
        # Extract the number
        match = re.search(r'Displaying (\d+) containers', displaying_text)
        if match:
            return int(match.group(1))
    return None

def main():
    count = fetch_container_count()
    if count is not None:
        print(f"Today's NVIDIA NIM container count: {count}")
    else:
        print("Couldn't find the container count.")

if __name__ == "__main__":
    main()
