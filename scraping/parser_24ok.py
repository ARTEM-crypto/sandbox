"""
    Parser for http://www.lady-maria.ru/collection/rasprodazha
"""


from my_requests import simple_get
from session_lol import lot_ajax, get_item_list
from bs4 import BeautifulSoup
import csv


root_url = "https://24-ok.ru/"
catalog_url = "https://24-ok.ru/catalog_new.php?catalog_id=2637997"
filename = 'tester.csv'
fields = ['наименование',
          'описание',
          'цена',
          'орг %',
          'ccылка на товар на сайте поставщика',
          'ссылки на Фото']

catalog_id = '2637997'
catalog_start = [None, "48"]
item_ids = []



# gather item ids
for start in catalog_start:
    raw_catalog_html = get_item_list(catalog_id, start)
    catalog_html = BeautifulSoup(raw_catalog_html, 'html.parser')
    items_html = catalog_html.select('div.block')
    for item in items_html:
        item_ids.append(item['id'][5:])



# write header
with open(filename, 'a', newline='', encoding='cp1251') as csvfile:
    fieldnames = fields
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()


# write rows for each product url
for id in item_ids:
    print(id)
    page_raw_html = lot_ajax(id, catalog_url)
    page_html = BeautifulSoup(page_raw_html, 'html.parser')
    page_imgs = page_html.select_one("#SP_fullres_image")["src"]
    page_name = page_html.select_one("h1").text.strip()
    # page_desc = page_html.select_one("table + p").text.strip().replace('\n', '')
    page_desc = page_html.select_one("p:nth-of-type(2)").text.strip().replace('\n', '')
    # page_weight = page_html.select_one("label").text.strip()
    page_cost = page_html.select_one(".catalogPrice").text.strip().replace('руб.', '')
    url = catalog_url + '&lot_id=' + id
    print("++++++++++++++++")
    print(page_desc)

    # write tow for each </tr>
    with open(filename, 'a', newline='', encoding='cp1251', errors='ignore') as csvfile:
        fieldnames = fields
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        writer.writerow({fields[0]: page_name,
                         fields[1]: page_desc,
                         fields[2]: page_cost,
                         fields[3]: 13,
                         fields[4]: url,
                         fields[5]: page_imgs})
