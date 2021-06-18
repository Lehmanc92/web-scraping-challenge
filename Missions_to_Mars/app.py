from flask import Flask, render_template, redirect
from bs4 import BeautifulSoup
import requests
import pymongo
from scrape_mars import scrape

app = Flask(__name__)

@app.route('/scrape')
def echo():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    collection = db.mars_info
    collection.drop()
    collection.insert_one(scrape())
    
    return redirect("/", code=302)