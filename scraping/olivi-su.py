"""
    Parser for http://www.lady-maria.ru/collection/rasprodazha
"""


from my_requests import simple_get
from bs4 import BeautifulSoup
import csv


def make_images(page, root_url):
    result = ''
    imgs = page.select('.product-item-detail-slider-controls-block.col-sm-4.col-sm-offset-1 img')
    for img in imgs:
        result += root_url + img['src'] + ' '

    if result.strip():
        return result
    else:
        img = page.select_one('.product-item-detail-slider-image img')
        return root_url + img['src'].strip()


def make_desk(page):
    mat_izd = 'Материал изделия:' + ' ' + page.select_one('.product-item-detail-properties-block.col-xs-14 .product-item-detail-properties-value').text.strip()
    mat_tex = 'Материал подкладки:' + ' ' +  page.select_one('.product-item-detail-properties-block.col-xs-14.col-xs-offset-1 .product-item-detail-properties-value').text.strip()

    divs = page.select('.product-item-detail-properties.col-xs-15')
    divs1 = page.select('.product-item-detail-properties.col-xs-15 + div')

    result = mat_izd + ', ' + mat_tex + '; '

    for i in range(len(divs)):
        result += (divs[i].text.strip() + ' ' +  divs1[i].text.strip()) + ', '
    desc = page.select_one('.description_container p').text.strip()

    return (result[:-2] + '; ' + desc).replace('\n','').replace('\n\r', '').replace('\r\n','')

def make_colors(page):
    result = ''
    lis = page.select('.product-item-detail-info-container .product-item-scu-item-list li')[:-1]
    for li in lis:
        result += li['title'] + ';'
    return result[:-1]



root_url = "https://olivi.su"
catalog_url = "https://olivi.su/catalog/rasprodazha/"
filename = 'tester.csv'
fields = ['наименование',
          'описание',
          'цена',
          'орг %',
          'ccылка на товар на сайте поставщика',
          'ссылки на Фото',
          'Цвет']
catalog_urls = [catalog_url]
for i in range(2, 4):
    catalog_urls.append(catalog_url + f"?PAGEN_1={i}")
urls = list()




# gather product urls
for url in catalog_urls:
    html = BeautifulSoup(simple_get(url), 'html.parser')
    for a in html.select('div.bx-content div.product-item a.product-item-image-wrapper'):
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
    page_imgs = make_images(page_html, root_url)
    page_name = page_html.select_one(".product-item-detail-title-model").text.strip()
    page_desc = make_desk(page_html)
    page_cost = page_html.select_one(".product-item-detail-price-current").text.strip()
    page_colors = make_colors(page_html)

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
                         fields[6]: page_colors})
