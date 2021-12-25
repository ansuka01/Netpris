
from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.juomavarasto.com/category/2/oluet").text
soup = BeautifulSoup(site, "html.parser")

divs = soup.find_all("h3", class_="H4 ProductName")
hinta = soup.find_all("div", class_="ProductPrices")
 
for row in divs:

    col = str(row).split(">")[-2]

    olut = str(col).split ("<")[0]

    print(olut)
