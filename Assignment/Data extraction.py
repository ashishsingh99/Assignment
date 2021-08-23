import sys
import requests
from bs4 import BeautifulSoup


req = requests.get("https://ec.europa.eu/programmes/horizon2020/en/h2020-section/information-and-communication-technologies")

soup = BeautifulSoup(req.content, "html.parser")

sys.stdout = open("myassignment.txt","w")

print(soup.get_text())

sys.stdout.close()