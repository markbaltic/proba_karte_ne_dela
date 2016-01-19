# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

params = {"originAirport": "MXP",
          "destinationAirport": "TFS",
          "departureDay": "2",
          "departureMonthYear": "082016",
          "isReturn": "false"
          }

result = requests.post(
    'http://www.easyjet.com/EN/FlightSelector.mvc//SearchForFlights',
    data = params)
