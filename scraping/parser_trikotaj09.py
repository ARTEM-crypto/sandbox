"""
    Parser for http://trikotazh09.ru/products
"""


from my_requests import simple_get
from bs4 import BeautifulSoup
import csv

def make_by_prop(page, prop):
    result = page.select('#product-params-view ul li')
    if result:
        size = ''
        for li in result:
            if prop in li.select_one('label').text:
                for option in li.select('select option')[1:]:
                    size += option.text + ';'
        if size:
            return size[:-1]
        else:
            return '-'
    else:
        return '-'

def make_desc(page):
    p = page.select_one('.user-inner p')
    if p:
        p_desc = p.text.strip()
    else:
        p_desc = ''

    tab_desc = page.select("#attributes table td")
    if tab_desc:
        keys = []
        values = []
        desc = ''
        for td in tab_desc[::2]:
            keys.append(td.select_one('span').text)
        for td in tab_desc[1::2]:
            values.append(td.text.strip())
        for i in range(len(keys)):
            desc += f'{keys[i]}: {values[i]}; '
        desc = desc[:-2]
    else:
        desc = ''
    return p_desc + "; " + desc




root_url = "http://trikotazh09.ru/"
catalog_url = "http://trikotazh09.ru/products/category/1943090"
filename = 'tester.csv'
fields = ['наименование',
          'описание',
          'цена',
          'орг %',
          'ccылка на товар на сайте поставщика',
          'ссылки на Фото',
          'Размер',
          'Цвет']
catalog_urls = [catalog_url]
for i in range(2, 4):
    catalog_urls.append(catalog_url + f"?page={i}")
urls = list()


# gather product urls
for url in catalog_urls:
    html = BeautifulSoup(simple_get(url), 'html.parser')
    for a in html.select('.product-item .product-link a'):
        if not a['href'] == '#':
            urls.append(a['href'])


# write header
# with open(filename, 'a', newline='', encoding='cp1251') as csvfile:
#     fieldnames = fields
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
#     writer.writeheader()


# write rows for each product url
for url in urls:
    print(url)
    page_html = BeautifulSoup(simple_get(url), 'html.parser')
    page_name = page_html.select_one('h1').text.strip()
    page_imgs = page_html.select_one('.avatar-view div.-relative img')['src']
    page_desc = make_desc(page_html)
    page_cost = page_html.select_one('#cost-by-impact span')['data-cost']
    page_sizes = make_by_prop(page_html, 'размер')
    page_colors = make_by_prop(page_html, 'цвет')

    print(repr(page_sizes),repr(page_colors))
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
                         fields[6]: page_sizes,
                         fields[7]: page_colors})
