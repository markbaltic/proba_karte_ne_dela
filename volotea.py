# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup


params = {
    "riptype":          "OneWay",
    "from":             "VCE",
    "to":               "KGS",
    "departuredate":    "2016-08-28",
    "bookingType":      "flight"
}


p = requests.post(
    'http://booking.volotea.com/Search.aspx?culture=en-GB',
    data=params)

soup = BeautifulSoup(p.text, "html.parser")

cene_po_datumih = {}
for div in soup.find_all('div', attrs={"class": "day-wrapper"}):
    for child in div.contents:
        cena_re = re.search(r'data-price-with-fee="€(.+?)"', str(child))
        date_re = re.search(r'data-date="(.+?)"', str(child))
        if cena_re and date_re:
            cena = float(cena_re.group(0).split('=')[1].replace('"', '').replace('€', ''))
            date = date_re.group(0).split('=')[1].split(' ')[0].replace('"', '')
            cene_po_datumih[date] = cena

print(cene_po_datumih)
