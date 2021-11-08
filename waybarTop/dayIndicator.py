import requests
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import datetime

url = 'https://web.bend.k12.or.us/abc/?site=shs'
r = requests.get(url)

parsed_html = BeautifulSoup(r.text, features="lxml")
day = parsed_html.body.find(id="name").text
#print(parsed_html.body.find(id="classes").text)

#data
cg = ['1', '3', '4', 'L', '6', '7']
cb = ['2', '3', '5', 'L', '6', '7']
cs = ['1', '2', '4', 'L', '5', '7']
ct = [[9, 37],[10, 59],[12,16],[12,56],[14,8],[15,25]]
ctw = [[9,19],[10,23],[11,22],[12,2],[12,56],[13,55]]

cdt = datetime.time()

#corects for days
ac = cg
if (day == "Black"):
    ac = cb
if (day == "Silver"):
    ac = cs

act = ct
#corects for wensday times
if datetime.date.today().weekday() == 2:
    act = ctw

now = datetime.datetime.now()
if(now<now.replace(hour=8, minute=25, second=0, microsecond=0)):
    print("gigaChronic")
else:
    print("good")