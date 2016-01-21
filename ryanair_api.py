import requests
import json


class RyanairAPI(object):
    def __init__(self):
        pass

    def get(self, origin, dest, mesec, leto):

        cene_po_datumih = {}
        for day in range(1, 31):
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


cena = RyanairAPI().get('TSF', 'CFU', '09', '2016')
print(cena)

#21.1.2016 :
#cene za julija
#{'2016-07-21': 57.99, '2016-07-28': 57.99, '2016-07-17': 57.99, '2016-07-24': 48.99, '2016-07-07': 48.99, '2016-07-31': 67.99, '2016-07-10': 48.99, '2016-07-03': 48.99, '2016-07-14': 40.99}
#cene za august:
#{'2016-08-28': 40.99, '2016-08-25': 48.99, '2016-08-07': 67.99, '2016-08-04': 67.99, '2016-08-11': 57.99, '2016-08-14': 67.99, '2016-08-18': 57.99, '2016-08-21': 48.99}
#cene za september:
#{'2016-09-15': 33.99, '2016-09-08': 33.99, '2016-09-11': 33.99, '2016-09-25': 33.99, '2016-09-22': 40.99, '2016-09-01': 40.99, '2016-09-29': 33.99, '2016-09-04': 33.99, '2016-09-18': 33.99}


