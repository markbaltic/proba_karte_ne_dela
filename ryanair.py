import requests
import json

leto = '2016'
mesec = '02'

cene_po_datumih = {}
for day in range(1, 29):
    if len(str(day)) < 2:
        day = '0' + str(day)
    datum_str = '%s-%s-%s' % (leto, mesec, str(day))
    print(datum_str)

    params = {
        "riptype":          "OneWay",
        "from":             "VLC",
        "to":               "TSF",
        "departuredate":    datum_str,
        "bookingType":      "flight"
    }

    r = requests.get(
        "https://desktopapps.ryanair.com/en-gb/availability?ADT=1&CHD=0&DateOut={0}&Destination={1}&FlexDaysOut=2&INF=0&Origin={2}&RoundTrip=false&TEEN=0".format(
            params['departuredate'], params['to'], params['from']))

    podatki = json.loads(r.text)

    if len(podatki['trips'][0]['dates'][0]['flights'])==0:
        pass
    else:
        redna_cena_danes = podatki['trips'][0]['dates'][0]['flights'][0]['regularFare']['fares'][0]['amount']
        cene_po_datumih[params['departuredate']] = redna_cena_danes

print(cene_po_datumih)
