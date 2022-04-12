import time
from attr import attr
from bs4 import BeautifulSoup
import requests
import numpy as np
import xlsxwriter as xlsx
import re



# BASE_URL = "https://www.searates.com"
# URL = "https://www.searates.com/tr/maritime/"
# request = requests.get(URL)
# soup = BeautifulSoup(request.content,'html5lib')
# countries = soup.findAll('li', attrs={'class': 'col-xs-6 col-md-3'})
# for country in countries:
#     countrylinks = BASE_URL + country.a['href']
#     print(countrylinks)


BASE_URL = "https://www.searates.com"
URL = "https://www.searates.com/tr/maritime/"


def getCountryLinks():
    request = requests.get(URL)
    soup = BeautifulSoup(request.content,'html5lib')
    clis = soup.findAll('li', attrs={'class': 'col-xs-6 col-md-3'})
    countrylink = []
    for country in clis:
        countrylink.append(BASE_URL + country.a['href'])
    return countrylink
        

def getPorts(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.content,'html5lib')
    countryports = soup.findAll('li', attrs={'class': 'col-xs-6 col-md-3'})
    cports = []
    for countryport in countryports:
        cports.append(BASE_URL + countryport.a['href'])
    return cports


def getPortDetails(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.content,'html5lib')
    portdetails = soup.findAll('tr')
    details = []
    for i in portdetails:
        details.append(i)
    return details
    


def allDetails():
    portlist = []
    for i in getCountryLinks():
        portlist.append(getPorts(i))
    return portlist



#list = []
#for i in allDetails(): # Her ülkedeki portlar ayrı array.
    list.append(i)


#tumu = []
#for i in list:
#    for z in i:
#        tumu += [z]


CLEANR = re.compile('<.*?>') 
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext


# workbook = xlsx.Workbook('Ports.xlsx')
# worksheet = workbook.add_worksheet()
#doc = open("data.txt","w")
#for i in tumu:
#    doc.write(str(getPortDetails(i)))
#    doc.write('\n')
#doc.close()


doc = open("data-play.txt","r")
stripped = open("stripped.txt","w")
for i in doc:
    stripped.write(i.replace(",","").replace('Telefon',',Telefon').replace('Port Detail','Port Detail,').replace('Fax',',Fax').replace('Address',',Address').replace('800 Number',',800 Number').replace('E-posta',',E-posta').replace('Latitude',',Latitude').replace('Longitude',',Longitude').replace('UN/',',UN/').replace('Port Type',',Port Type').replace('General Information','').replace('First Port',',First Port').replace('ETA',',ETA').replace('Publication',',Publication').replace('Chart',',Chart').replace('Representative',',Representative').replace('Medical',',Medical').replace('Harbor Characteristics',',Harbor Characteristics').replace('Harbor Size',',Harbor Size').replace('Shelter',',Shelter').replace('Maxiumum Vessel',',Maxiumum Vessel').replace('Harbor Type',',Harbor Type').replace('Turning Area',',Turning Area').replace('Good Holding',',Good Holding').replace('Entrance Restrictions',',Entrance Restrictions').replace('Tide',',Tide').replace('Overhead Limit',',Overhead Limit').replace('Swell',',Swell').replace('Other',',Other').replace('Water Depth',',Water Depth').replace('Channel:',',Channel').replace('Cargo Pier',',Cargo Pier').replace('Mean Tide',',Mean Tide').replace('Anchorage',',Anchorage').replace('Oil Terminal',',Oil Terminal').replace('Pilotage',',Pilotage').replace('Compulsory',',Compulsory').replace('Available',',Available').replace('Advisable',',Advisable').replace('Local Assist',',Local Assist').replace('Tugs',',Tugs').replace('Assist',',Assist').replace('Salvage',',Salvage').replace('Quarantine',',Quarantine').replace('Pratique',',Pratique').replace('Other',',Other').replace('Deratt Cert',',Deratt Cert').replace('Communications',',Communications').replace('Telephone',',Telephone').replace('Radio',',Radio').replace('Air:',',Air:').replace('Telegraph',',Telegraph').replace('Radio Tel',',Radio Tel').replace('Rail:',',Rail:').replace('Loading &',',Loading &').replace('Wharves',',Wharves').replace('Med Moor',',Med Moor').replace('Ice',',Ice').replace('Anchor',',Anchor').replace('Beach',',Beach').replace('Lifts &',',Lifts &').replace('100 + Ton Lifts',',100 + Ton Lifts').replace('50-100 Ton Lifts',',50-100 Ton Lifts').replace('25-49 Ton Lifts',',25-49 Ton Lifts').replace('0-24 Ton Lifts',',0-24 Ton Lifts').replace('Fixed Cranes',',Fixed Cranes').replace('Mobile Cranes',',Mobile Cranes').replace('Floating Cranes',',Floating Cranes').replace('Longshore',',Longshore').replace('Electrical Repair',',Electrical Repair').replace('Steam',',Steam').replace('Electrical',',Electrical').replace('Navigation Equipment',',Navigation Equipment').replace('Supplies',',Supplies').replace('Provisions',',Provisions').replace('Fuel Oil',',Fuel Oil').replace('Deck',',Deck').replace('Water',',Water').replace('Diesel Oil',',Diesel Oil').replace('Engine',',Engine').replace('Repairs, Drydock, Railway & Other Services',',Repairs, Drydock, Railway & Other Services').replace('Ship Repairs',',Ship Repairs').replace('Marine Railroad Size',',Marine Railroad Size').replace('Degauss',',Degauss').replace('Drydock Size',',Drydock Size').replace('Garbage Disposal',',Garbage Disposal').replace('Dirty Ballast',',Dirty Ballast').replace('Max Draft',',Max Draft').replace('Port Size:',',Port Size:').replace('Port Services','').replace('Department of Marine and','Department of Marine and Port Services'))
stripped.close()
print('ok')

#doc = open("stripped.txt")
#for i in doc:
#    print(i)
#    time.sleep(1000)