"""
    Parser for https://viotex-37.ru
"""


from my_requests import simple_get
from bs4 import BeautifulSoup
import csv


def make_desc(test_page_html):
    sostav = test_page_html.select('div.catalog_addonfield_sostav div')
    tkan = test_page_html.select('div.catalog_addonfield_tkan div')
    otdelka = test_page_html.select('div.catalog_addonfield_otdelka div')
    result = ''
    if len(sostav) > 0:
        result += (sostav[0].text + ' ')
    if len(tkan) > 0:
        result += (tkan[0].text + ' ')
    if len(otdelka) > 0:
        result += (otdelka[0].text + ' ')
    return result

def make_final_desk(page_desk, table_row_desc):
    if table_row_desc.strip():
        return page_desk.strip() + "; " + table_row_desc.replace("\n", ", ")
    else:
        return page_desc.strip()



root_url = "https://viotex-37.ru/"
catalog_url = "https://viotex-37.ru/tekstil-dlya-vannoy/polotenca"
raw_html = simple_get(catalog_url)
urls = list()
filename = 'tester.csv'
fields = ['наименование',
          'описание',
          'цена',
          'орг %',
          'ccылка на товар на сайте поставщика',
          'ссылки на Фото',
          'Размер']

# gather product urls
html = BeautifulSoup(raw_html, 'html.parser')
for a in html.select('div.catalog_list_one a'):
    urls.append(root_url + a['href'])

# write header
with open(filename, 'a', newline='', encoding='cp1251') as csvfile:
    fieldnames = fields
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()


# write rows for each product url
for url in urls:
    page_raw_html = simple_get(url)
    page_html = BeautifulSoup(page_raw_html, 'html.parser')
    page_img = url + page_html.select('div.main_photo img')[0]['src']
    page_name = page_html.select('div.catalog_one_title h1')[0].text.strip()
    page_desc = make_desc(page_html)
    trs = page_html.findAll("tr", class_='catalog_size_count') # find all html table rows in the page
    trs = [tr for tr in trs if not len(tr['class'][1]) > 1] # filter out invisible table rowsl, tr['class'] is a list of classes of </tr>.

    # write tow for each </tr>
    with open(filename, 'a', newline='', encoding='cp1251') as csvfile:
        fieldnames = fields
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        for tr in trs:
            size = tr.select('span.size-title')[0].text
            cost = tr.select('td:nth-of-type(4)')[0].text
            table_row_desc = tr.select('td:nth-of-type(2)')[0].text
            final_desk = make_final_desk(page_desc, table_row_desc)
            writer.writerow({fields[0]: page_name,
                             fields[1]: final_desk,
                             fields[2]: cost,
                             fields[3]: 13,
                             fields[4]: url,
                             fields[5]: page_img,
                             fields[6]: size})
