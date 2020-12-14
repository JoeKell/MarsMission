#Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


executable_path = {'executable_path': 'C:/Users/Joe/bin/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
time.sleep(5)
html = browser.html
soup = bs(html, 'html.parser')
Titles=soup.find_all('div', class_='content_title')
Ps=soup.find_all('div', class_='article_teaser_body')
News_Title=Titles[1].text
News_P=Ps[0].text

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
base_url='https://www.jpl.nasa.gov'
time.sleep(5)
html = browser.html
soup = bs(html, 'html.parser')
Pic_url=str(soup.find('article', class_='carousel_item'))
a=Pic_url.find("url('")+5
b=Pic_url.find(".jpg")+4
url_ending=Pic_url[a:b]
FeaturedImage=base_url+url_ending

url = 'https://space-facts.com/mars/'
#I learned this method from this article: https://towardsdatascience.com/scraping-tabular-data-with-pandas-python-10cf2a133cbf
Mars_Facts=pd.read_html(url)[0].rename(columns={0:"Metric", 1: "Value"})
MF_Table=Mars_Facts.to_html()

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
base_url='https://astrogeology.usgs.gov/'
time.sleep(5)
html = browser.html
soup = bs(html, 'html.parser')
Item_List=soup.find_all('div', class_='description')
hemisphere_image_urls=[]

for item in Item_List:
    item_Name=str(item.find('a').text).replace(" Enhanced","")
    url_ending=item.find('a')['href']
    full_url=base_url+url_ending
    browser.visit(full_url)
    time.sleep(5)
    subhtml = browser.html
    subsoup = bs(subhtml, 'html.parser')
    item_Image=base_url+subsoup.find('img', class_="wide-image")['src']
    hemisphere_image_urls.append({"title":item_Name,"img_url":item_Image})

browser.quit()

Scrape_Dict={"Headline":News_Title,"Text":News_P,"Featured Image":FeaturedImage,"Fact Table":MF_Table,"Hemisphere Images":hemisphere_image_urls }