#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
from pprint import pprint


# In[2]:


def init_browser():
    
    executable_path = {"executable_path":"C:\Program Files\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless = False)


# # NASA Mars News

# In[3]:


def mars_news():
    browser = init_browser()
    
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = bs(html,"html.parser")

    mars_title = soup.find("div",class_="content_title").text
    mars_paragraph  = soup.find("div", class_="article_teaser_body").text

    news=[]
    news_dict={'Title': mars_title,
              'Description': mars_paragraph
              }
    news.append(news_dict)
    
    browser.quit()
    
    return news
    


# In[4]:




# # JPL Mars Space Images - Featured Image

# In[5]:


def mars_image():
    browser = init_browser()
    
    jpl_url ="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    
    featured_img_url_raw = soup.find("div", class_="carousel_items").find("article")["style"]
    featured_img_url_raw = featured_img_url_raw.split("'")[1]
    
    base_url= "https://www.jpl.nasa.gov"
    featured_img_url= base_url + featured_img_url_raw
    
    browser.quit()
    
    return featured_img_url


# In[6]:




# # Mars Weather

# In[7]:


def mars_weather():
    browser = init_browser()
    
    twitter_url ="https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    
    mars_weather_data = (soup.find(class_="tweet-text")).get_text()
    
    browser.quit()
    
    return mars_weather_data


# In[8]:




# # Mars Facts

# In[9]:


def mars_facts():
    browser = init_browser()
    
    facts_url="https://space-facts.com/mars/"
    
    table = pd.read_html(facts_url)
    stats_table=table[1]
    
    stats_html=stats_table.to_html(header=False, index=False).replace('\n', '')
    
    browser.quit()
    
    return stats_html


# In[10]:




# # Mars Hemispheres

# In[11]:


def mars_hemispheres():
    browser = init_browser()
    
    hemisphere_url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    
    hemi_names=[]
    links=soup.find_all('h3')

    for hemi in links:
        hemi_names.append(hemi.text)

    hemi_urls=[]

    for hemi in hemi_names:
        hemi_dict ={}
        browser.click_link_by_partial_text(hemi)
        hemi_dict['title'] = hemi
        hemi_dict['img_url'] = browser.find_by_text('Sample')['href']
        hemi_urls.append(hemi_dict)
        browser.back()
        
    browser.quit()

    return hemi_urls


# In[12]:




# In[15]:


def scrape():
    
    mars_news_scrape=mars_news()
    mars_image_scrape=mars_image()
    mars_weather_scrape=mars_weather()
    mars_facts_scrape=mars_facts()
    mars_hemispheres_scrape=mars_hemispheres()
    
    mars_info={'Mars_News': mars_news_scrape,
               'Featured_Image': mars_image_scrape,
               'Mars_Weather': mars_weather_scrape,
               'Mars_Facts': mars_facts_scrape,
               'Mars_Hemispheres': mars_hemispheres_scrape
              }
    return mars_info


# In[16]:




# In[ ]:




