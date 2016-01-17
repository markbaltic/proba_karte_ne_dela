import requests
import json


class RyanairAPI(object):

    def get(cls, origin, dest, mesec, leto):

        cene_po_datumih = {}
        for day in range(1, 29):
            if len(str(day)) < 2:
                day = '0' + str(day)
            datum_str = '%s-%s-%s' % (leto, mesec, str(day))

            r = requests.get(
                "https://desktopapps.ryanair.com/en-gb/availability?ADT=1&CHD=0&DateOut={0}&Destination={1}&FlexDaysOut=2&INF=0&Origin={2}&RoundTrip=false&TEEN=0".format(
                    datum_str, dest, origin))

            podatki = json.loads(r.text)

            if len(podatki['trips'][0]['dates'][0]['flights']) == 0:
                pass
            else:
                redna_cena_danes = podatki['trips'][0]['dates'][0]['flights'][0]['regularFare']['fares'][0]['amount']
                cene_po_datumih[datum_str] = redna_cena_danes

        return cene_po_datumih


# cena = RyanairAPI().get('BGY', 'KGS', '08', '2016')
# print(cena)
