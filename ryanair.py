import requests
import json

stn = "STN"
r = requests.get("https://desktopapps.ryanair.com/en-gb/availability?ADT=1&CHD=0&"
                 +"DateOut=2016-03-16&"
                 +"Destination={0}&FlexDaysOut=2&INF=0&".format(stn)
                 +"Origin=TRS&RoundTrip=false&TEEN=0"
    )
##print(r.text)
##
podatki = json.loads(r.text)
print(podatki)


if len(podatki['trips'][0]['dates'][0]['flights'])==0:
    print("Ni leta")
else:
    redna_cena_danes = podatki['trips'][0]['dates'][0]['flights'][0]['regularFare']['fares'][0]['amount']
    print(redna_cena_danes)
