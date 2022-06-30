# Importing libraries 
from distro import like
import requests #Gets us the html data
from bs4 import BeautifulSoup #Scrapes the html data
import lxml
import pandas as pd #We will store all our data in a pandas dataframe

headers = {'User-Agent': 'Mozilla/5.0'} #Mimicing a browser visit
html = requests.get("https://old.reddit.com/r/datascience/", headers=headers).text #Getting the HTML code of the community

#Using BeautifulSoup for scraping the HTML code
soup = BeautifulSoup(html, "lxml") #Entering our HTML code into BeautifulSoup 

#Finding data about posts
attrs = {'class': 'thing'}

for post in soup.find_all('div', attrs=attrs): #For everypost
    # Some values are None so we put it in a try and except
    try:
        title = post.find('a', class_ = "title").text #Title of the post
        flair = post.find("span", class_ = "linkflairlabel").text #Flair title of the post
        upvotes = post.find("div", class_ = "score unvoted").text #No. of upvotes
        no_comments = post.find("a", class_ = "comments").text #No. of comments

        #Replacing . with None
        if upvotes == "•" : 
            upvotes = "None"
        if no_comments == "comments" : 
            no_comments = "0 comments"
    except:
        continue