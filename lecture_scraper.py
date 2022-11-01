import bs4
import requests
import requests.compat
import unittest

from pathlib import Path

def fetch_links(url):
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    #return (link.get('href') for link in soup.find_all("a"))
    for link in soup.find_all("a"):
        yield requests.compat.urljoin(url, link.get('href'))

def download(url, name):
    req = requests.get(url)
    with open(name, 'wb') as f:
        f.write(req.content)

class lecture_test(unittest.TestCase):
    def test_download(self):
        test_out = Path("downloads/test_lec00.pdf")
        test_out.parent.mkdir(parents=True, exist_ok=True)
        download("https://statmech.stanford.edu/teaching/2020a_chem263/lecture01_notes.pdf", test_out)
    def test_fetch_links(url):
        links = fetch_links("https://statmech.stanford.edu/teaching/2021a_chem263/")
        for link in links:
            print(link)

if __name__ == "__main__":
    print("running lecture_scrapter")
    unittest.main()
