#importing libraries
import bs4 as BeautifulSoup
import urllib.request 

def fetchArticle(url = 'https://en.wikipedia.org/wiki/20th_century'):
    #fetching the content from the URL
    fetched_data = urllib.request.urlopen(url)

    article_read = fetched_data.read()

    #parsing the URL content and storing in a variable
    article_parsed = BeautifulSoup.BeautifulSoup(article_read,'html.parser')

    #returning <p> tags
    paragraphs = article_parsed.find_all('p')

    article_content = ''

    #looping through the paragraphs and adding them to the variable
    for p in paragraphs:  
        article_content += p.text
    return article_content
    
def writeContentToFile(url = 'https://en.wikipedia.org/wiki/20th_century'):
    temp = url.split('/')
    filename = temp[len(temp)-1]
    print(filename)
    text = fetchArticle(url)
    targetfile = open("./Paragraphs/Wiki_"+filename+".txt","w")
    targetfile.writelines(text)
    targetfile.close()