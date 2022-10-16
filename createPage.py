from bs4 import BeautifulSoup
import requests
import re


def getTags():
    url = "https://www.maxhager.xyz/"
    name = requests.get(url)
    soup = BeautifulSoup(name.content)
    startWithAddingElemToList = False
    domElem = []
    h3Elem = []
    finalElem = []
    for elem in soup.find_all():
        elem = str(elem)
        if elem == '<h2 id="currently-doing">Currently doing</h2>':
            startWithAddingElemToList = True
        if elem == '<h2 id="finished">Finished</h2>':
            break
        elif startWithAddingElemToList == True:
            domElem.append(elem)
    for elem in domElem:
        if elem[:3] == "<h3":
            h3Elem.append(elem)
    for i in h3Elem:
        x = re.findall('id=".*"', i)
        finalElem.append(x)
    for i in finalElem:
        i[0] = i[0][4:-1]
    finalElem = finalElem[1:]
    return finalElem


def addToPage(elem):
    html = """
    <head>
    <title>New Tab</title>
    </head>
    <ul style="list-style-type:none; font-size:300%; text-align:center; margin:0; padding:0; position:absolute; top:50%; left:50%; transform:translate(-50%, -50%);">
    das ist ein  test
    """
    for i in elem:
        html = html + "<li>" + i[0] + "</li>\n"
    with open("/Users/maxhager/Projects2022/ChromeProjectsOverview/index.html", "w") as file:
        file.write(html)


if __name__ == "__main__":
    tags = getTags()
    addToPage(tags)
