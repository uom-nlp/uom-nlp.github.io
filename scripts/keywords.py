from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

input="../_data/papers.yml"
output="abstract.txt"

num_errors = 0
num_pubs = 0

output_file = open(output, "w")
for line in tqdm(open(input).readlines()):

    line = line.strip()

    if line.startswith("docurl") and "aclweb" in line:

        site = line[(line.index("\"")+1):-1]
        page = requests.get(site)
        soup = BeautifulSoup(page.content, "html.parser")
        x = soup.find("button", attrs={"class": "btn btn-clipboard btn-secondary btn-sm d-none"})
        abstract = [item for item in x.attrs["data-clipboard-text"].split("\n") if item.strip().startswith("abstract")]
        try:
            abstract = abstract[0][(abstract[0].index("\"")+1):-2]
            output_file.write(abstract + "\n")
            output_file.flush()
            num_pubs += 1
        except:
            num_errors += 1
            pass

output_file.close()

print("Number of publications =", num_pubs)
print("Number of errors =", num_errors)

