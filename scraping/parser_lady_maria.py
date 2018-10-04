"""
    Parser for http://www.lady-maria.ru/collection/rasprodazha
"""


from my_requests import simple_get
from bs4 import BeautifulSoup
import csv

def make_images(divs):
    images_str = ''
    for div in divs:
        images_str += f"{div['href']} "
    return images_str[:-1]

def make_sizes(spans):
    sizes = ''
    for span in spans:
        sizes += span['title'] + '; '
    return sizes[:-2]

def get_colors(divs):
    correct = None
    for div in divs:
        if 'Цвет' in div.__str__():
            correct = div
    if not correct:
        return '-'
    return correct.select_one('span:nth-of-type(2)').__str__().replace('<span>', '').replace('</span>','').strip().replace(' ','').replace('\n', '').replace(',','; ')



root_url = "http://www.lady-maria.ru/"
catalog_url = "http://www.lady-maria.ru/collection/rasprodazha"
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
for i in range(2, 54):
    catalog_urls.append(catalog_url + f"?page={i}")
urls = list()


# gather product urls
for url in catalog_urls:
    html = BeautifulSoup(simple_get(url), 'html.parser')
    for a in html.select('div.card-image a.image-inner'):
        urls.append(root_url + a['href'])

# write header
with open(filename, 'a', newline='', encoding='cp1251') as csvfile:
    fieldnames = fields
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()


# write rows for each product url
for url in urls:
    print(url)
    page_raw_html = simple_get(url)
    page_html = BeautifulSoup(page_raw_html, 'html.parser')
    page_imgs = make_images(page_html.select('div.gallery-top div.swiper-wrapper div.swiper-slide'))
    page_name = page_html.select('h1.product-title')[0].text.strip()
    page_desc = page_html.select('div.info-head div.info-target.editor')[0].text.replace('\r\n', ' ').strip()
    page_sizes = make_sizes(page_html.select('div.option-values span.option-value.is-span'))
    page_cost = page_html.select_one('div.product-price span').__str__().replace('<span data-product-price="">', '').replace('руб</span>', '').strip()
    page_colors = get_colors(page_html.select('div.props .property'))

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
