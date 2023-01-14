import requests
from datetime import date
import time
import pandas as pd

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 1000)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/50.0.2661.102 Safari/537.36'}
res = requests.get('https://gsmartfleet.com/api/api.php?api=user&ver=1.0&key=FBF307CF3D7DEB5E227D76F2D5195641&cmd=USER_GET_OBJECTS', headers=headers)

data = res.json()

stopDate = time.strptime(str(date.today()), "%Y-%m-%d")
startDate = time.strptime('2021-04-27', "%Y-%m-%d")

table = pd.DataFrame()

print(data[0])
# print('hi')

for i in data:
    date = i['dt_tracker']
    splitDate = date.split()[0]

    if splitDate == '0000-00-00':
        pass
    else:
        newDate = time.strptime(splitDate, "%Y-%m-%d")

    if startDate < newDate < stopDate:

        try:
            table2 = pd.DataFrame({
                'Last_Connection': [i['dt_tracker']],
                'Sim_No': [i['sim_number']],
                'Owner_No': [i['custom_fields'][15]['value']],
                'Reg_Number': [i['name']],
                'Active': [i['active']],
                'Expiry ': [i['object_expire_dt']],
               # 'Active': [i['active']],
               # 'Charge': [i['params']['charge']],
              #  'Power': [i['params']['power']],
                'Owner': [i['custom_fields'][17]['value']],
            })
            table = table.append(table2)
        except IndexError:
            print(IndexError(i))
            pass

table['Last_Connection'] = pd.DataFrame(table.Last_Connection)
table.sort_values(by=['Last_Connection'], inplace=True, ascending=False)
table = table.reset_index()
print(table)

#exportTableData = table.to_excel("Vehicles Offline Report.xlsx", sheet_name="Vehicles Offline Report", engine='xlsxwriter')


