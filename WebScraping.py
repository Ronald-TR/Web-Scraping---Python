import requests
from bs4 import BeautifulSoup

def ScrapDigitalDropsIn(category=''):
    if category.__eq__(''):
        return 'Insert a category'
    URL_BASE = 'http://digitaldrops.com.br/category/' + category
    HTML_BASE = requests.get(URL_BASE)
    if HTML_BASE.status_code != 200:
        return 'Error, category or connection not found'
    posts = BeautifulSoup(HTML_BASE.content, 'html.parser')
    posts = posts.find_all('div', class_='et-description')
    return posts


myScrap = ScrapDigitalDropsIn('robo')
      #show the quantity of posts in the category, which in this case, are inside of the <h2> tag,
      #from the divs with the class='et-description'.   
print('Number of posts: ' + str(myScrap.__len__())) 

for title in myScrap: #each <div class='et-description'> in the tuple result
      #Just plain text, yours and any tag.
    contentTitle = title.find('h2').get_text() 
      #just the href value in each first <a> inside of the <h2> tag
    linkToPost = title.find('h2').find('a', href=True)['href'] 
      #print title and the link to the full post inline
    print('Title: ' + contentTitle + '. Link: ' + linkToPost)

#print(myScrap) #print the result without scrapping
