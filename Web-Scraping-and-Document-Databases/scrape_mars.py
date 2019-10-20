#!/usr/bin/env python
# coding: utf-8

# In[68]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
from pprint import pprint


# In[72]:


# Define function to initialize browser
def init_browser():
    
    executable_path = {"executable_path":"C:\Program Files\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless = False)


# # NASA Mars News

# In[73]:


# Define function to scrape Mars news
def mars_news():
    browser = init_browser()
    
#Visit URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

# Scrape page into soup
    html = browser.html
    soup = bs(html,"html.parser")

# Find news title and paragraph
    mars_title = soup.find("div",class_="content_title").text
    mars_paragraph  = soup.find("div", class_="article_teaser_body").text
    
#Create an empty news list and append news dict
    news=[]
    news_dict={'Title': mars_title,
              'Description': mars_paragraph
              }
    news.append(news_dict)
    
    browser.quit()
    
    return news
    

# # JPL Mars Space Images - Featured Image

# In[75]:


# Define function to scapr Mars featured image
def mars_image():
    browser = init_browser()

# Visit URL
    jpl_url ="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

# Scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')
    
# Find image URL and format accordingly
    featured_img_url_raw = soup.find("div", class_="carousel_items").find("article")["style"]
    featured_img_url_raw = featured_img_url_raw.split("'")[1]
    
    base_url= "https://www.jpl.nasa.gov"
    featured_img_url= base_url + featured_img_url_raw
    
    browser.quit()
    
    return featured_img_url

# # Mars Weather

# In[77]:


# Define function to scrape Mars weather
def mars_weather():
    browser = init_browser()

# Visit URL
    twitter_url ="https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)

# Scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

# Get the Mars weather tweet text
    mars_weather_data = (soup.find(class_="tweet-text")).get_text()
    mars_weather_data = mars_weather_data.replace('\n', ' ').replace('pic',',').split(",")[0]
    
    browser.quit()
    
    return mars_weather_data

# # Mars Facts

# In[81]:


# Define a function to scrape Mars facts
def mars_facts():
    browser = init_browser()
    
    facts_url="https://space-facts.com/mars/"

# Scrape table into pandas
    table = pd.read_html(facts_url)
    stats_table=table[1]

# Convert table info ibto HTML
    stats_html=stats_table.to_html(header=False, index=False).replace('\n', '')
    
    browser.quit()
    
    return stats_html

# # Mars Hemispheres

# In[83]:


# Define funtion to find Mars hemispheres info
def mars_hemispheres():
    browser = init_browser()

# Visit URL
    hemisphere_url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)

# Scrape page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

# Create a list to hold hemisphere names and append names to list
    hemi_names=[]
    links=soup.find_all('h3')

    for hemi in links:
        hemi_names.append(hemi.text)

# Create a list to hold hemisphere names and URL's
    hemi_urls=[]

# Visit each hemisphere site and append to the dict...append dict to list
    for hemi in hemi_names:
        hemi_dict ={}
        browser.click_link_by_partial_text(hemi)
        hemi_dict['title'] = hemi
        hemi_dict['img_url'] = browser.find_by_text('Sample')['href']
        hemi_urls.append(hemi_dict)
        browser.back()
        
    browser.quit()

    return hemi_urls

# In[87]:


# Define a function that scrapes all Mars info
def scrape():
    
    mars_news_scrape=mars_news()
    mars_image_scrape=mars_image()
    mars_weather_scrape=mars_weather()
    mars_facts_scrape=mars_facts()
    mars_hemispheres_scrape=mars_hemispheres()

# Define a mars_info dict to hold all information from the scrape
    mars_info={'Mars_News': mars_news_scrape,
               'Featured_Image': mars_image_scrape,
               'Mars_Weather': mars_weather_scrape,
               'Mars_Facts': mars_facts_scrape,
               'Mars_Hemispheres': mars_hemispheres_scrape
              }
    return mars_info





