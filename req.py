import requests


class RyanairAPI(object):

    def get(cls, origin, dest, date_out, date_in):
        r = requests.get(
            'https://desktopapps.ryanair.com/en-gb/availability?ADT=1&CHD=0&DateOut=2016-04-04&' +
            'Destination=%s&FlexDaysOut=2&INF=0&Origin=%s&RoundTrip=false&TEEN=0' % (origin, dest)
        )

    def parse_results(cls, r):
        result = r.json()['trips']
        for trip in result:
            for date in trip['dates']:
                for flight in date:
                    print(flight)


class SkyScannerAPI(object):
    def get(cls, origin, dest, date_out, date_in):
        # Request URL:http://www.skyscanner.net/trck/Day%20View/request.ashx?trackingLang=EN&pageReferrer=http%3A%2F%2Fwww.skyscanner.net%2F&request=5d3ab91b-40ac-4b5b-852b-f14903dc73d1_Fri,%2008%20Jan%202016%2009:37:57%20GMT&oplace=BUD&iplace=LPA&adults=1&children=0&infants=0&odate=2016-11-02&idate=2016-11-16&nodename=SSPVWUK1NWF029&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false
        # http://business.skyscanner.net/portal/en-GB/Documentation/Authentication
        # API doc: http://business.skyscanner.net/portal/en-GB/Documentation/FlightsLivePricingList

        # //*[@id="day-section"]/div/div[3]/ul/li[1]/article/div[2]/div[2]/a[1]
        pass


##
##origin = 'BGY'
##dest = 'KSG'
##api_list = [RyanairAPI, SkyScannerAPI]
##for api in api_list:
##    args = {}
##    api.get(**args)
