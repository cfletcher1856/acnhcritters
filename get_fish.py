#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re
import base64

class Fish(object):
    pass

def getDateRange(data):
    d=[]
    for x in range(6,18):
        d.append(False if data[x] == '-' else True)

    r=[]
    ctr=1
    for x in d:
        if x:
            r.append(ctr)
        ctr=ctr+1
    return r

def thing(months):
    reverse_months = months[len(months)::-1]
    # print("%"*50)
    # print(months)
    if not all(months):
        if months[0] and months[11]:
            # print('{0} - {1}'.format(month_names[abs(reverse_months.index(False)-12)], abs(reverse_months.index(False)-13)))
            # print('{0} - {1}'.format(month_names[months.index(False)-1], months.index(False)))
            return (abs(reverse_months.index(False)-13), months.index(False))
        else:
            # print('{0} - {1}'.format(month_names[months.index(True)], months.index(True)+1))
            # print('{0} - {1}'.format(month_names[abs(reverse_months.index(True)-11)], abs(reverse_months.index(True)-12)))
            return (months.index(True)+1, abs(reverse_months.index(True)-12))
    else:
        return (1,12)
    # print("%"*50)

def calculateTime(time, index):
    if ' - ' not in time:
        return None

    timesplit = time.split(' - ', 1)
    if 'PM' in timesplit[index]:
        return int(re.sub('\D', '', timesplit[index])) + 12
    else:
        return int(re.sub('\D', '', timesplit[index]))

url="https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)"
headers = requests.utils.default_headers()
headers.update({'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'lxml')

div = soup.find('div', attrs={'class':'tabbertab','title':'Northern Hemisphere'})
table = div.find('table', class_='roundy')
rows = table.find_all('tr')

for row in rows[2:]:
    print('*'*50)
    cols = row.find_all('td')
    img = row.find('img')
    data = [col.text.rstrip("\n").strip() for col in cols]
    active_months = getDateRange(data)
    # start_month, stop_month = thing(active_months)
    f = Fish()
    f.name = data[0]
    # f.image_64 = base64.b64encode(requests.get(re.sub('\.png.*', '.png', img.get('data-src'))).content)
    # f.image_url = re.sub('\.png.*', '.png', img.get('data-src'))
    f.price = data[2]
    f.location = data[3]
    f.time = data[5]
    f.start_time = calculateTime(data[5], 0)
    f.end_time = calculateTime(data[5], 1)
    f.allday = True if data[5] == 'All day' else False
    f.active_months = active_months
    # f.start_month = start_month
    # f.stop_month = stop_month
    # f.months = active_months
    # f.jan = active_months[0]
    # f.feb = active_months[1]
    # f.mar = active_months[2]
    # f.apr = active_months[3]
    # f.may = active_months[4]
    # f.jun = active_months[5]
    # f.jul = active_months[6]
    # f.aug = active_months[7]
    # f.sep = active_months[8]
    # f.oct = active_months[9]
    # f.nov = active_months[10]
    # f.dec = active_months[11]

    print(vars(f))

    print('*'*50)


# start = 12
# end = 3
# today = 4

# print(start <= today or end >= today)

# x = range(6,18)

# for i in x:
#     print(i)

