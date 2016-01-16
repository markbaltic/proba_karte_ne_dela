import requests
import re
from bs4 import BeautifulSoup
import re


parametri = {
    "riptype":"OneWay",
    "from":"VCE",
    "fromTyper":"Venice · VCE",
    "to":"KGS",
    "toTyper":"Kos · KGS",
    "salida":"Tuesday, June 28 2016",
    "departuredate":"2016-06-28",
    "returndate":"2016-06-28",
    #"from2":,
    "fromTyper2":"Please choose departure airport",
    #"to2":,
    "toTyper2":"Please choose destination airport",
    "departuredate0":"2016-01-30",
    "adults_select":"1",
    "adults":"1",
    "children":"0",
    "infants":"0",
    #"tipoFamilia":,
    #"promo":,
    "bookingType":"flight"
    }

s = requests.Session()
r = s.get("http://booking.volotea.com/Search.aspx?culture=en-GB")
p = s.post("http://booking.volotea.com/Search.aspx?culture=en-GB", data = parametri)

soup1 = BeautifulSoup(r.text,"html.parser")
soup2 = BeautifulSoup(p.text, "html.parser")

# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>") #mogoce bom rabu

##cena = r'<span class="racun">(.*?)\s*=\s*</span>'
cena_vzorec = r'<span class="price regular left">€(.*?)</span>'
cena = re.search(cena_vzorec, soup2.find_all('a')).group(1)
print(cena)

#print(soup2.find_all('a').next_sibling)

#print(soup2)





##with open('spletna_volotea_brezparam.txt', 'w') as f:
##    print(soup1, file=f)

##with open('spletna_volotea_param.html', 'w') as f:
##    print(p.text, file=f)
