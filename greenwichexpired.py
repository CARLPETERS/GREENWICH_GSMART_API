import requests
from datetime import date
import time
import pandas as pd

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 1000)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/50.0.2661.102 Safari/537.36'}
res = requests.get(
    'https://gsmartfleet.com/api/api.php?api=user&ver=1.0&key=FBF307CF3D7DEB5E227D76F2D5195641&cmd=USER_GET_OBJECTS',
    headers=headers)

data = res.json()

stopDate = time.strptime(str(date.today()), "%Y-%m-%d")
startDate = time.strptime('2019-01-01', "%Y-%m-%d")

table = pd.DataFrame()

print(data[0])
# print('hi')

a = 0
b = 0
d = 0
c=0
for i in data:
    c = c+1
    date = i['dt_tracker']
    splitDate = date.split()[0]

    if splitDate == '0000-00-00':
        d = d+1
        pass
    else:
        newDate = time.strptime(splitDate, "%Y-%m-%d")

    if startDate <= newDate <= stopDate:

        try:

            if not i['custom_fields']:
                print(b,'NO CUSTOM FIELDS', [i['name']])
                b = b + 1

                pass

            else:
                if not i['custom_fields'][9]['value']:
                    print('himmmmmmm')
                    pass
                table2 = pd.DataFrame({
                    'Last_Connection': [i['dt_tracker']],
                    'Sim_No': [i['sim_number']],
                    'Reg_Number': [i['name']],
                    'Active': [i['active']],
                    'Expiry ': [i['object_expire_dt']],
                    'Owner': [i['custom_fields'][17]['value']],
                    # 'Active': [i['active']],
                    # 'Charge': [i['params']['charge']],
                    #  'Power': [i['params']['power']],

                    'Serial No': [i['custom_fields'][9]['value']],
                    'Owner_No': [i['custom_fields'][12]['value']],
                })
                table = table.append(table2)
        except IndexError:
            # if not i['custom_fields'][9]['value']:
            table4 = pd.DataFrame({
                'Last_Connection': [i['dt_tracker']],
                'Sim_No': [i['sim_number']],
                'Reg_Number': [i['name']],
                'Active': [i['active']],
                'Expiry ': [i['object_expire_dt']],
                'Serial No': i['custom_fields'][9]['value'],
                'Owner': [' '],
                'Owner_No': [i['custom_fields'][12]['value']],

            })
            table = table.append(table4)
            # else:
            #     table3 = pd.DataFrame({
            #         'Last_Connection': [i['dt_tracker']],
            #         'Sim_No': [i['sim_number']],
            #         'Reg_Number': [i['name']],
            #         'Active': [i['active']],
            #         'Expiry ': [i['object_expire_dt']],
            #         # 'Serial No ': i['custom_fields'][9]['value'],
            #         'Owner': [' '],
            #         'Owner_No': [i['custom_fields'][12]['value']],
            #
            #     })
            #
            # table = table.append(table3)
            # print(IndexError(i))

            print(a, 'TRY EXEMPTED', [i['name']])
            a = a + 1
            pass

table['Active'] = pd.DataFrame(table.Active)
table.sort_values(by=['Active'], inplace=True, ascending=False)
table = table.reset_index()
print(table)
print("TRY EXEMPTED",a)
print("no custom",b)
print('000000', d)
print('total data', c)

print(table.duplicated())

exportTableData = table.to_excel("Vehicles Expired Report.xlsx", sheet_name="Vehicles Expired Report",
                                 engine='xlsxwriter')

# for i in data:
#     car = db.query(models.Car).filter(models.Owner.regno == ''.join([i['name']])).first()
#     if not car:
#         try:
#             if not i['custom_fields']:
#                 pass
#             else:
#                 fname = [i['custom_fields'][17]['value']][0].split()[0]
#                 lname = [i['custom_fields'][17]['value']][0].split()[1]
#                 regno = ''.join([i['name']])
#                 idno = [i['custom_fields'][15]['value']][0]
#                 telno = [i['custom_fields'][12]['value']][0]
#                 nationality = 'Kenyan'
#                 email = [i['custom_fields'][4]['value']][0]
#                 addressno = 600
#                 addresstown = 'Nairobi'
#
#                 save_to_db(fname, lname, regno, idno, telno,
#                            nationality, email, addressno, addresstown)
#
#         except IndexError:
#             # print(i['name'])
#             fname = [i['custom_fields'][15]['value']][0]
#             lname = last_name([i['custom_fields'][15]['value']][0])
#             regno = ''.join([i['name']])
#             idno = [i['custom_fields'][12]['value']][0]
#             telno = [i['custom_fields'][11]['value']][0]
#             nationality = 'Kenyan'
#             email = [i['custom_fields'][4]['value']][0]
#             addressno = 600
#             addresstown = 'Nairobi'
