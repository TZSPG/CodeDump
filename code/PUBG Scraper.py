import requests
from bs4 import BeautifulSoup
import re
from os import system


r = requests.get('http://outage.report/playerunknowns-battlegrounds')

soup = BeautifulSoup(r.content, 'html.parser')
text_tag = str(soup.find('text'))

num_of_outages = re.findall(re.compile('>\d+<'), text_tag)
num_of_outages = int(num_of_outages[0].strip('<').strip('>'))

if num_of_outages > 200:
    print('PUBG is down')
else:
    print('Go play some PUBG')

system('pause')