
# THIS PROGRAM PRINTS ALL THE VEHICLES THAT ARE TRANSMITTING

import requests
from datetime import date
import time
import pandas as pd

from datetime import datetime
from pytz import timezone

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 1000)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/50.0.2661.102 Safari/537.36'}
res = requests.get('https://gsmartfleet.com/api/api.php?api=user&ver=1.0&key=FBF307CF3D7DEB5E227D76F2D5195641&cmd'
                   '=USER_GET_OBJECTS', headers=headers)

# FBF307CF3D7DEB5E227D76F2D5195641
# D17D73B851E8080EC83A438702C964C0

data = res.json()

# print(data)

stopDate = time.strptime(str(date.today()), "%Y-%m-%d")
startDate = time.strptime('2022-8-01', "%Y-%m-%d")

table = pd.DataFrame()

# print(data[0])
# print('hi')

# Current time in UTC
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
fmtt = "%Y-%m-%d %H:%M:%S"
now_utc = datetime.now(timezone('UTC'))
print (now_utc.strftime(fmt))

# Convert to US/Pacific time zone
now_pacific = now_utc.astimezone(timezone('Africa/Nairobi'))
print (now_pacific.strftime(fmt))


for i in data:
    date = i['dt_tracker']



    splitDate = date.split()[0]

    if splitDate == '0000-00-00':
        pass
    else:
        newDate = time.strptime(splitDate, "%Y-%m-%d")

        if startDate < newDate <= stopDate:
            # print(i)
            try:
                table2 = pd.DataFrame({
                    'Last_Connection': [i['dt_tracker']],
                    'Reg_Number': [i['name']],
                    'Sim_No': [i['sim_number']],
                    'Owner_No': [i['custom_fields'][15]['value']],
                    'Owner': [i['custom_fields'][17]['value']],
                    'Serial_No': [i['custom_fields'][9]['value']],
                    'Active': [i['active']]
                    #'Charge': [i['params']['charge']],
                  #  'Power': [i['params']['power']]
                })
                table = table.append(table2)
            except IndexError:
                table3 = pd.DataFrame({
                    'Last_Connection': [i['dt_tracker']],
                    'Reg_Number': [i['name']],
                    'Active': [i['active']],
                    'Sim_No': [i['sim_number']]
                })
                table = table.append(table3)
                pass

table['Last_Connection'] = pd.DataFrame(table.Last_Connection)
table.sort_values(by=['Last_Connection'], inplace=True, ascending=False)
table = table.reset_index()
print(table)

reportExcel = table.to_excel("LasTt Connection reports.xlsx", sheet_name="Last Connection Report", engine='xlsxwriter')

print('done')