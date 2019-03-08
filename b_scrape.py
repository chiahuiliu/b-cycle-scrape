import requests
from bs4 import BeautifulSoup
import csv
import collections
import re
import pandas as pd
import time
import certifi
import urllib3
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
#Headers will make it look like you are using a web browser
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

def scrape():
    res = []
    for i in range (0,3376,10):
        url = 'https://austin.bcycle.com/stations/station-locations'
        time.sleep(3)
        response = requests.get(url, headers=headers, verify=False).text
        soup = BeautifulSoup(response, "lxml")
        for s in soup.find_all("div", attrs={'class': 'markerContent markerAvailable'}):
            res.append(s)
    print(res[0])
    print(len(res))

if __name__ == '__main__':
    scrape()
