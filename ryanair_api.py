import requests
import json


class RyanairAPI(object):
    def __init__(self):
        pass

    def get(self, origin, dest, mesec, leto):

        cene_po_datumih = {}
        for day in range(1, 30):
            print(day)
            if len(str(day)) < 2:
                day = '0' + str(day)
            datum_str = '%s-%s-%s' % (leto, mesec, str(day))

            r = requests.get(
                "https://desktopapps.ryanair.com/en-gb/availability?ADT=1&"
                "CHD=0&DateOut=%s&Destination=%s&FlexDaysOut=2&INF=0&"
                "Origin=%s&RoundTrip=false&TEEN=0" % (datum_str, dest, origin))

            podatki = json.loads(r.text)

            if len(podatki['trips'][0]['dates'][0]['flights']) == 0:
                pass
            else:
                redna_cena_danes = podatki['trips'][0]['dates'][0]['flights'][0]['regularFare']['fares'][0]['amount']
                cene_po_datumih[datum_str] = redna_cena_danes

        return cene_po_datumih


##cena = RyanairAPI().get('TSF', 'CFU', '08', '2016')
##print(cena)
