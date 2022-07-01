# Importing libraries 
import requests #Gets us the html data
from bs4 import BeautifulSoup #Scrapes the html data
import lxml
import csv #We will convert our data to CSV
import time

#Getting user data
community = str(input("Which subreddit to scrape(Case-sensitive): "))
posts_scrape = int(input("Number of posts to scrape(Whole-number): "))


headers = {'User-Agent': 'Mozilla/5.0'} #Mimicing a browser visit
url = "https://old.reddit.com/r/" + community + "/"
html = requests.get(url, headers=headers).text #Getting the HTML code of the community

#Using BeautifulSoup for scraping the HTML code
soup = BeautifulSoup(html, "lxml") #Entering our HTML code into BeautifulSoup 

counter = 1

while (counter <= posts_scrape):
    posts = soup.find_all('div', attrs = {'class': 'thing'})

    for post in posts:
        # Some values are None so we put it in a try and except
        try:
            title = post.find('a', class_ = "title").text #Title of the post
            flair = post.find("span", class_ = "linkflairlabel").text #Flair title of the post
            upvotes = post.find("div", class_ = "score unvoted").text #No. of upvotes
            no_comments = post.find("a", class_ = "comments").text #No. of comments

            #Replacing Null values
            if upvotes == "•" : 
                upvotes = "None"
            if no_comments == "comments" : 
                no_comments = "0 comments"
        except:
            continue

        fields = [title, flair, upvotes, no_comments] #Listing the fields
    
    #Exporting to CSV
        with open('output.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
        counter += 1

    #Add more posts from other pages
    next_button = soup.find("span", class_="next-button")
    next_page_link = next_button.find("a").attrs['href']
    time.sleep(2)
    html = requests.get(next_page_link, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
