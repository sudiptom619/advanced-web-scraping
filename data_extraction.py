

from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

with open('/Users/sudiptomitra/Desktop/advanced-web-scraping/smartprix.html', 'r', encoding='utf=8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
names = []
prices = []
ratings = []
sim = []
processor = []
ram = []
battery = []
display = []
camera = []
card = []
os = []



container = soup.find_all('div', {'class' : "sm-product has-tag has-features has-actions"})
print(len(container), 'hello')
for i in container:
    try:
        names.append(i.find('h2').text)
    except:
        names.append(np.nan)

    try:
        prices.append(i.find('span',{'class': 'price'}).text)

    except:
        prices.append(np.nan)

    try:
        ratings.append(i.find('span',{'class': 'sm-rating'})['style'].split(" ")[-1].replace(';',""))
    except:
        ratings.append(np.nan)

    list_items = i.find('ul',{'class':'sm-feat specs'}).find_all('li')

    try:
        sim.append(list_items[0].text)
    except:
        sim.append(np.nan)
    try:
        processor.append(list_items[1].text)
    except:
        processor.append(np.nan)
    try:
        ram.append(list_items[2].text)
    except:
        ram.append(np.nan)
    try:
        battery.append(list_items[3].text)
    except:
        battery.append(np.nan)
    try:
        display.append(list_items[4].text)
    except:
        display.append(np.nan)
    try:
        camera.append(list_items[5].text)
    except:
        camera.append(np.nan)
    try:
        card.append(list_items[6].text)
    except:
        card.append(np.nan)
    try:
        os.append(list_items[7].text)
    except:
        os.append(np.nan)


# print(soup.prettify())
#
df = pd.DataFrame({
    'model':names,
    'price':prices,
    'rating':ratings,
    'sim':sim,
    'processor':processor,
    'ram':ram,
    'battery':battery,
    'display':display,
    'camera':camera,
    'card':card,
    'os':os
})
print(df.sample(5))
df.to_csv('smartprix.csv')
df.to_excel('smartprix.xlsx',engine='xlsxwriter')
