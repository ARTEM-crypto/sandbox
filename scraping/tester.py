from my_requests import simple_get
from bs4 import BeautifulSoup
import csv

url = "https://olivi.su/catalog/zhenskie_sumki/670_sumka_zhenskaya/"
page_html = BeautifulSoup(simple_get(url), 'html.parser')
result = page_html.select("#attributes table td")

print(result)
