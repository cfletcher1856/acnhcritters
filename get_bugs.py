#!/usr/bin/env python3
#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import re
import base64

month_names = [
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December'
]


class Bug(object):
    pass

def getDateRange(data):
    d=[]
    for x in range(5,17):
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

url="https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)"
headers = requests.utils.default_headers()
headers.update({'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'lxml')

div = soup.find('div', attrs={'class':'tabbertab','title':'Northern Hemisphere'})
t = div.find('table', class_='roundy')
table = t.find('table')
rows = table.find_all('tr')

for row in rows[2:]:
    print('*'*50)
    # print(row)
    cols = row.find_all('td')
    # print(cols)
    img = row.find('img')
    data = [col.text.rstrip("\n").strip() for col in cols]
    print(data)
    active_months = getDateRange(data)
    start_month, stop_month = thing(active_months)
    b = Bug()
    b.name = data[0]
    # b.image_64 = base64.b64encode(requests.get(re.sub('\.png.*', '.png', img.get('data-src'))).content)
    # b.image_url = re.sub('\.png.*', '.png', img.get('data-src'))
    b.price = data[2]
    b.location = data[3]
    b.time = data[4]
    b.start_time = calculateTime(data[4], 0)
    b.end_time = calculateTime(data[4], 1)
    b.allday = True if data[4] == 'All day' else False
    b.active_months = active_months
    # b.start_month = start_month
    # b.stop_month = stop_month
    # b.months = active_months
    # b.jan = active_months[0]
    # b.feb = active_months[1]
    # b.mar = active_months[2]
    # b.apr = active_months[3]
    # b.may = active_months[4]
    # b.jun = active_months[5]
    # b.jul = active_months[6]
    # b.aug = active_months[7]
    # b.sep = active_months[8]
    # b.oct = active_months[9]
    # b.nov = active_months[10]
    # b.dec = active_months[11]

    print(vars(b))

    print('*'*50)


# start = 12
# end = 3
# today = 4

# print(start <= today or end >= today)

# x = range(6,18)

# for i in x:
#     print(i)



