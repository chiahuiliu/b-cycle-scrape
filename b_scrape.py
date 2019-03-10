import requests
from bs4 import BeautifulSoup
import time
import certifi
import urllib3
import os
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
import datetime as dt
import time

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

def get_results(url, time_now):
    response = requests.get(url, headers=headers, verify=False).text
    soup = BeautifulSoup(response, "lxml")
    main_text = soup.find_all("div", attrs={'id': 'MainBg2'})
    str_main_text = str(main_text)
    time_now = str(time_now).split('.')[0]
    time_now = time_now.replace(' ', '_')
    time_now = time_now.replace(':', '_')
    filename = './raw_data/raw_data_'+str(time_now)+'.csv'
    with open(filename, "w") as f:
        f.write(str_main_text)
        print('Successfully saved '+str(filename))

if __name__ == '__main__':
    while(dt.datetime.now() < dt.datetime.strptime('2019-03-25  12:00:00', '%Y-%m-%d %H:%M:%S')):
        get_results('https://austin.bcycle.com/stations/station-locations', dt.datetime.now())
        time.sleep(1800)
