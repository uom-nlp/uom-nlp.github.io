from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

input = "karin-pubmed.xml"
page = open(input).read()

soup = BeautifulSoup(page, "html.parser")
for di, d in enumerate(soup.findAll("description")):
    if di > 3 and di < 23:
        print(d.text[d.text.find("<p>Abstract<br/>")+16:d.text.rfind("<br/>")].replace("<br/>", " "))
