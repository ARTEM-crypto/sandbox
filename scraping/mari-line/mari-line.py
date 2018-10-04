"""
    Parser for http://www.mari-line.com/catalog/
"""

from my_requests.my_requests import simple_get
from my_requests.session_lol import get_items
from bs4 import BeautifulSoup
import csv



 

root_url = "http://www.mari-line.com"
catalog_url = "http://www.mari-line.com/catalog/blouses/"
catalog_url = "http://www.mari-line.com/catalog/blouses/"
filename = 'tester.csv'
fields = ['наименование',
          'описание',
          'цена',
          'орг %',
          'ccылка на товар на сайте поставщика',
          'ссылки на Фото',
          'Размер']


def get_imgs(page):
    result = ""
    for img in page.select('#showcase span img'):
        result += root_url + img['src'] + " "
    return result


def get_desc1(page):
    result = None
    characts = page.select('.b-characteristics > div')
    for div in characts:
        if 'Состав' in  div.select_one('.key').text:
            result = div.select_one('.val').text.strip()
    if result:
        return ' ' + 'Состав: ' + result
    else:
        return ''

def get_desc(page):
    desc = page_html.select_one(".b-item-description p")

    if desc:
        return desc.text.strip().replace('\n', '') + get_desc1(page_html)
    else:
        return get_desc1(page_html)
        
    

def get_sizes(page):
    sizes = page.select('div.b-showcase-sizes > div')
    result = ''

    for size in sizes:
        if 'Нет в наличии' not in str(size.get('title')):
            result += size.select_one('label').text.strip() + '; '

    return result[:-2]


# gather product urls
urls = []
dresses = open('dresses.html', 'r')
html = BeautifulSoup(dresses.read(), 'html.parser')
for a in html.select('.b-catalog-list-item .b-showcase-link'):
    urls.append(root_url + a['href'])

# write header
with open(filename, 'a', newline='', encoding='cp1251') as csvfile:
    fieldnames = fields
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

# # write rows for each product url
for url in urls:
# for url in ['http://www.mari-line.com/catalog/dresses/7196']:
    print(url)
    page_raw_html = simple_get(url)
    page_html = BeautifulSoup(page_raw_html, 'html.parser')
    page_name = page_html.select_one(".b-showcase-desc-bg h1").text.strip() + ' ' + \
                page_html.select_one(".b-showcase-desc-bg h2").text.strip()
    page_imgs = get_imgs(page_html)
    page_desc = get_desc(page_html)
    page_size = get_sizes(page_html)
    
    cost = page_html.select_one('.b-prices .b-prices-value')
    cost_sale = page_html.select_one('.b-prices .b-prices-sale')

    if cost_sale:
        page_cost = cost_sale.text.strip()
    else:
        page_cost = cost.text.strip() if cost else ''

    # write row for each page
    with open(filename, 'a', newline='', encoding='cp1251', errors='ignore') as csvfile:
        fieldnames = fields
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        writer.writerow({fields[0]: page_name,
                         fields[1]: page_desc,
                         fields[2]: page_cost,
                         fields[3]: 13,
                         fields[4]: url,
                         fields[5]: page_imgs,
                         fields[6]: page_size})

print(len(urls))