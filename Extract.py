from bs4 import BeautifulSoup
import codecs

soup = BeautifulSoup(open("superbowl.html", encoding="utf8"), 'html.parser')

f = file = codecs.open('CleanedSuperbowl.html', "w", "utf-8")


dataset = []
for row in soup.find_all("tr")[+1:]:
    for td in row.find_all("td"):
        dataset = td.get_text()
        f.write(dataset)