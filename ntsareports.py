import pandas as pd

pd.set_option('display.max_rows', 2450000)
pd.set_option('display.max_columns', 2450000)
pd.set_option('display.width', 45610000)
#pd.set_option('mode.chained_assignment', None)

data = pd.read_csv('eventss.csv')


def filterEvent(event):
    return data[(data.event == event)]


gps = filterEvent('No GPS')
signal = filterEvent('Signal Disconnected')
overspeed = filterEvent('overspeed')
powercut = filterEvent('Power Cut')
powerconnect= filterEvent('Power Connected')


def sort(table):
    print("step 1")
    return table.sort_values(by=['object'], inplace=True, ascending=False)



def filterTable(table):
    print('done 2')
    return table.drop_duplicates(subset="object")


sort(gps)
sort(signal)
sort(overspeed)
sort(powercut)
sort(powerconnect)
filterGps = filterTable(gps)
filterSignal = filterTable(signal)
filterPowerCut = filterTable(powercut)
filterPowerConnect = filterTable(powerconnect)

speed = {}

for i in overspeed.index:
    if overspeed['object'][i] not in speed:
        speed[overspeed['object'][i]] = overspeed['speed'][i]

for j in speed:
    for i in overspeed.index:
        if overspeed['object'][i] == j and overspeed['speed'][i] > speed[j]:
            speed[j] = overspeed['speed'][i]

filterOverspeed = filterTable(overspeed)

for j in speed:
    for i in filterOverspeed.index:
        if filterOverspeed['object'][i] == j and overspeed['speed'][i] < speed[j]:
            filterOverspeed['speed'][i] = speed[j]


report = pd.concat([filterGps, filterOverspeed, filterSignal, filterPowerCut, filterPowerConnect])

reportExcel = report.to_excel("violation reports.xlsx", sheet_name="Violation Report", engine='xlsxwriter')

print('done')