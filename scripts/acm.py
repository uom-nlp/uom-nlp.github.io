from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

inputs = ["pubs/trevor.html", "pubs/tim.html", "pubs/daniel.html", "pubs/lea.html", "pubs/jeyhan.html"]

for input in inputs:
    page = open(input).read()

    soup = BeautifulSoup(page, "html.parser")
    for di, d in enumerate(soup.findAll("div", attrs={"class": "abstract"})):
        print(d.text)
