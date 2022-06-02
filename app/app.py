import crochet
crochet.setup()

from flask import Flask, jsonify
from flask import render_template
from flask import request
import pymongo
from pymongo import MongoClient
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from bson import json_util, ObjectId
import json
import sys
sys.path.insert(1, '/app/crawler/crawler/spiders')
from extractor import ExtractorSpider

app = Flask(__name__)
output_data = []
crawl_runner = CrawlerRunner()
url = None


def get_db():
    client = MongoClient(host='mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["links_db"]
    collection = db['links']
    return collection

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/scrape", methods=['POST'])
def scrape():
    global url
    try:
        if request.method == 'POST':
            url = request.form.get('url')
        if len(url) > 0:
            scrape_with_crochet(url=url)
            page_sanitized = json.loads(json_util.dumps(output_data))
            return  render_template('scraped.html',string=page_sanitized, url=url)
        else:
            return   render_template('error.html'), 412
    except:
        return   render_template('error.html'), 412


@crochet.wait_for(timeout=500.0)
def scrape_with_crochet(url):
    global output_data
    output_data=[]
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(ExtractorSpider,start_urls=url)
    return eventual  


def _crawler_result(item, response, spider):
    global output_data
    collection = get_db()
    try:
        for i in [item]:
            collection.replace_one({'name': i['name']}, i,True)
            output_data.append(i)
    except:
        pass

@app.route("/list", methods=['POST','GET'])
def lists():
    collection = get_db()
    cursor = collection.find()
    try:
        page_sanitized = json.loads(json_util.dumps(cursor))
        return render_template('list.html',string=page_sanitized)
    except:
        return   render_template('error.html'), 505
    
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)
