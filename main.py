from volotea_api import VoloteaAPI
from ryanair_api import RyanairAPI

api_list = {
    'VoloteaAPI': VoloteaAPI,
    'RyanairAPI': RyanairAPI
    }

cene_po_datumu = {}
for ime_api, api in api_list.items():
    result = api().get('BGY', 'KGS', '08', '2016')
    for datum in result:
        if datum not in cene_po_datumu:
            cene_po_datumu[datum] = {}
        cene_po_datumu[datum][ime_api] = result[datum]

print(cene_po_datumu)
