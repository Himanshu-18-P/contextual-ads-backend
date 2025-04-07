# https://www.gq.com/story/best-sneakers-of-2025
from core.api import *

from flask import Flask

def create_app():
    app = Flask(__name__)
    return app 

if __name__ == "__main__":
    # app = create_app()
    # app.run(debug=True)

    start  = Start()
    url = 'https://www.gq.com/story/best-sneakers-of-2025'
    res = start.tag_data(url)
    res = dict(res)
    res['url'] = url
    print(res)