"""
    Parser http://vasilek-omsk.ru/
"""

from my_requests import simple_get
from bs4 import BeautifulSoup
import csv

def make_desk(page):
    result = ''
    divs = page.select('.description div.options .option')
    for div in divs:
        result += div.select_one('span').__str__().replace('<span>','').replace('</span>', '')
        result += ' ' + div.select_one('input')['value'] + '; '
    desc = page.select_one('#tab-description p')
    result += desc.text.strip().replace('\n\r\n', ' ').replace('\r\n', " ").replace('\t', ' ').replace('\n', ' ').replace('\n\n', ' ')
    return result


def make_sizes(page):
    result = ''
    sizes = page.select('select option')[1:]
    for size in sizes:
        result += size.text.strip() + ';'
    return result[:-1]

def make_colors(page):
    colors = page.select('.description div.options .option')[-1].select_one('input')['value']
    return colors.replace(',', ';')[:-1]



root_url = "http://vasilek-omsk.ru"
catalog_url = "http://vasilek-omsk.ru/shapky/"
filename = 'tester.csv'
fields = ['наименование',
          'описание',
          'цена',
          'орг %',
          'ccылка на товар на сайте поставщика',
          'ссылки на Фото',
          'Размер']

catalog_urls = [catalog_url]
pages = 0
if pages > 0:
    for i in range(2, pages+1):
        catalog_urls.append(catalog_url + f"?page={i}")
urls = list()

# gather product urls
for url in catalog_urls:
    html = BeautifulSoup(simple_get(url), 'html.parser')
    for a in html.select('div.image a'):
        urls.append(a['href'])

# # write header
# with open(filename, 'a', newline='', encoding='cp1251') as csvfile:
#     fieldnames = fields
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
#     writer.writeheader()


for url in urls:
    print(url)
    page_raw_html = simple_get(url)
    page_html = BeautifulSoup(page_raw_html, 'html.parser')
    page_name = page_html.select_one('h1').text.strip()
    page_desc = make_desk(page_html)
    print(repr(page_desc))
    page_cost = page_html.select_one('.price').__str__().replace('<div class="price">Цена:', '').replace('<br>\n</br></div>', '').strip().replace('р.','').strip()
    # page_colors = make_colors(page_html)
    page_sizes = make_sizes(page_html)
    page_imgs = page_html.select_one('#image')['src']

    # write tow for each </tr>
    with open(filename, 'a', newline='', encoding='cp1251', errors='ignore') as csvfile:
        fieldnames = fields
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        writer.writerow({fields[0]: page_name,
                         fields[1]: page_desc,
                         fields[2]: page_cost,
                         fields[3]: 13,
                         fields[4]: url,
                         fields[5]: page_imgs,
                         fields[6]: page_sizes})
