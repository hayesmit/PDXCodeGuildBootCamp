import requests
from bs4 import BeautifulSoup
import json

source = requests.get('https://cookieandkate.com/?s=quinoa').text

soup = BeautifulSoup(source, 'lxml')

myRecipes = {}
for article in soup.findAll('article'):
    #get next url
    url = article.find('a')
    #get title of the dish to make
    title = url.text
    print(title)
    if title == '':
        continue
    
    url_href = url['href']
    #print(url['href'])
    open_link = requests.get(url_href).text
    new_page = BeautifulSoup(open_link, 'lxml')
    #print(new_page.prettify())
    correctHeading = new_page.findAll('script', type='application/ld+json')
    recipeInformation = json.loads(correctHeading[1].text)
    ingredients = ', '.join(recipeInformation['recipeIngredient'])
    print(ingredients)
    print('\n')
    instructions = ', '.join(recipeInformation['recipeInstructions'])
    print(instructions)
    print('\n\n')
    myRecipes[title] = [ingredients, instructions]

    #get title
    #title = article.find('a')
    #print(title['href'])

#what problem your application solve? what is the core function it performs?
#how did you go about planning?
#what major issues did you encounter during the course of development? how did you go about overcoming them?
#how did your vision for the project change over time?
#what part did you like the most? least?
#what is the future of the project? what features (if any) will you work on next?




#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
