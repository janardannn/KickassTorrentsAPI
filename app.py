from KickAssAPI import KickAssAPI
from flask import Flask, request, jsonify

API = KickAssAPI()

app = Flask(__name__)

@app.route('/')
def index():
    return 'KickAssAPI up and running!'

@app.route('/search')
def search():
    torrent = request.args.get('torrent')
    if torrent:
        resp = API.search(torrent)
        return jsonify(resp)
    else:
        return jsonify({'error': 'No query provided'})

@app.route('/magnet')
def magnet():
    page_url = request.args.get('page_url')
    if page_url:
        magnet_link = API.magnet(page_url)
        return jsonify({'magnet': magnet_link})
    else:
        return jsonify({'error': 'No magnet provided'})

if __name__ == '__main__':
    app.run(debug=True)