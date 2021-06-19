from flask import Flask, render_template, redirect
from bs4 import BeautifulSoup
import requests
import pymongo
from scrape_mars import scrape

app = Flask(__name__)

@app.route('/')
def default():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    collection = db.mars_info
    info = collection.find_one()
    images = info['hemisphere_images']
    
    return render_template('index.html', listings=info, hemisphere_images=images)
    



@app.route('/scrape')
def scrape_mars():

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    collection = db.mars_info
    collection.drop()
    collection.insert_one(scrape())

    return redirect("/")





if __name__ == '__main__':
    app.run(debug=True)