# ABOUT

This is a unofficial API for KickassTorrents. It uses Python requests module and BeautifulSoup 4 to get the webpage(s) and to find the magnet links present in the webpage(s).

It is in early development stage, so the features available are very less but it gets the job done.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from KickAssAPI import API

api = API()
results = api.search("Attack on Titan")

for result in results:
    print("Title: ",result.text)
    print("Link: ",result.get('href'))
```

```python
from KickAssAPI import API

api = API()
results = api.search("Attack on Titan")

magnet_link  = api.magnet(results,index=1)
print(magnet_link)
```
