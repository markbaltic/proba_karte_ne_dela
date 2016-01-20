from volotea_api import VoloteaAPI
from ryanair_api import RyanairAPI
import csv

api_list_1 = {
    'VoloteaAPI': {"ime": VoloteaAPI,
                   "origin": 'VCE',
                   "dest": 'CFU',
                   "mesec": '08',
                   "leto": '2016'
                   },
##    'RyanairAPI': {"ime": RyanairAPI,
##                   "origin": 'TSF',
##                   "dest": 'CFU',
##                   "mesec": '08',
##                   "leto": '2016'
##                   }
    }

cene_po_datumu = {}
for ime_api, api in api_list_1.items():
    result = api["ime"]().get(api["origin"], api["dest"], api["mesec"], api["leto"])
    for datum in result:
        if datum not in cene_po_datumu:
            cene_po_datumu[datum] = {}
        cene_po_datumu[datum][ime_api] = result[datum]

print(cene_po_datumu)

##cene_po_datumu = {}
##ime_api = 'VoloteaAPI'
##result = api_list[ime_api]().get('VCE', 'CFU', '08', '2016')
##for datum in result:
##    if datum not in cene_po_datumu:
##        cene_po_datumu[datum] = {}
##    cene_po_datumu[datum][ime_api] = result[datum]
##
##ime_api = 'RyanairAPI'
##result = api_list[ime_api]().get('TSF', 'CFU', '08', '2016')
##for datum in result:
##    print(datum)
##    if datum not in cene_po_datumu:
##        cene_po_datumu[datum] = {}
##    cene_po_datumu[datum][ime_api] = result[datum]


writer = csv.writer(open('dict.csv', 'wb'))
for key, value in cene_po_datumu.items():
   writer.writerow([key, value])
