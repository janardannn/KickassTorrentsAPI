import requests
from bs4 import BeautifulSoup

class API():
        
    def search(self,query) -> dict:

        """ Returns a list of dictionaries with the results of the search """

        url = "https://katcr.to/usearch/" + query + "/"
        results = requests.get(url)
        soup = BeautifulSoup(results.text, "html.parser")
        self.results = soup.find_all("a", {"class": "cellMainLink"})

        return self.results


    def magnet(self,search_dict,index=0) -> str:

        """ Returns the magnet link of the selected torrent """

        magnet_page = requests.get("https://katcr.to"+search_dict[index].get("href")) 
        magnet_page_bs = BeautifulSoup(magnet_page.text, "html.parser")
        magnet_link = magnet_page_bs.find("a", {"class": "kaGiantButton"}).get("href")

        return magnet_link 