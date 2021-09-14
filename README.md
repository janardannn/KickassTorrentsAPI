# ABOUT

This is a unofficial API for KickassTorrents.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Search for torrents using the API
```python
from KickAssAPI import KickAssAPI

api = KickAssAPI()
results = api.search("Attack on Titan")

for key in results:
    print(results[key]['title'])
    print(results[key]['page_url'])
```

Get the magent link of a selected torrent from search results 
```python
from KickAssAPI import KickAssAPI

api = KickAssAPI()
results = api.search("Attack on Titan")

magnet_link  = api.magnet(results[index]['page_url'])
print(magnet_link)
```

## API

Using the [API](https://kickass-api-unofficial.herokuapp.com/) deployed on Heroku

Searching for torrents using the API
```python
import requests, json

API_SEARCH = "https://kickass-api-unofficial.herokuapp.com/search?torrent="

resp = requests.get(API_SEARCH + "Attack on titan")
results = json.loads(resp.text)

for key in results:
    print(results[key]['title'])
    print(results[key]['page_url'])
```

Getting magnet links using the API
```python
import requests, json

API_MAGNET = "https://kickass-api-unofficial.herokuapp.com/magnet?page_url="

page_url = results[index]['page_url']
resp = requests.get(API_MAGNET+page_url)

magnet = json.loads(resp.text)

magnet_link = magnet['magnet']
```
