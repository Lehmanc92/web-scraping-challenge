# Importing dependencies

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# Setting up path

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)



def scrape_article():
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')   

    article_title = soup.find('div', class_='content_title')
    article_blurb = soup.find('div', class_="article_teaser_body")

    return [article_title.text, article_blurb.text]


def scrape_image():
    # Setting new URL for different website

    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Finding the featured image and grabbing the url for it
    featured_image_url = soup.find('img', class_="headerimage fade-in")['src']

    return featured_image_url



def scrape_facts_tables():
    # Setting new URL for different website

    url = "https://galaxyfacts-mars.com/"

    # Pulling facts from table, then re-reading them to html

    facts_tables = pd.read_html(url)

    mars_facts_df = facts_tables[1]

    return mars_facts_df.to_html()



def scrape_hemispheres():
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/valles.html"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/cerberus.html"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/schiaparelli.html"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/syrtis.html"},
    ]
    return hemisphere_image_urls

def scrape():
    article_title, article_blurb = scrape_article()
    featured_img_url = scrape_image()
    mars_facts = scrape_facts_tables()
    hemisphere_images = scrape_hemispheres()

    return {"article_title" : article_title, "article_blurb" : article_blurb, "featured_img_url" : featured_img_url, "mars_facts" : mars_facts, "hemisphere_images" : hemisphere_images }

