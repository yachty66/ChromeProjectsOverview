from bs4 import BeautifulSoup
import requests 

#go to https://www.maxhager.xyz/ and get every tag between first h2 tags 
def getTags():
    #soup = BeautifulSoup(html_doc, 'html.parser')
    #go to https://www.maxhager.xyz/ and get every tag between first h2 tags with beaitiful soup
    url = "https://www.maxhager.xyz/"
    name = requests.get(url)
    soup = BeautifulSoup(name.content) 
    print(soup.prettify())
    
    #get everything from <a href="#currently-doing"> to  <a href="#finished"> from soup
    
    pass

#add all tags as elements in a table in index.html -- centered and visible
def addToPage():
    pass

if __name__ == "__main__":
    getTags()
