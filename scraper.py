# Importing libraries 
from attr import fields
from distro import like
import requests #Gets us the html data
from bs4 import BeautifulSoup #Scrapes the html data
import lxml
import csv #We will convert our data to CSV

headers = {'User-Agent': 'Mozilla/5.0'} #Mimicing a browser visit
html = requests.get("https://old.reddit.com/r/datascience/", headers=headers).text #Getting the HTML code of the community

#Using BeautifulSoup for scraping the HTML code
soup = BeautifulSoup(html, "lxml") #Entering our HTML code into BeautifulSoup 

for post in soup.find_all('div', attrs = {'class': 'thing'}): #For everypost
    
    #For getting header on CSV
    title = "title"
    flair = "flair"
    upvotes = "upvotes"
    no_comments = "no_comments"

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

    fields = [title, flair, upvotes, no_comments]
    #Exporting to CSV
    with open('output.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)