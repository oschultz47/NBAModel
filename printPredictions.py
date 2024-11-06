import pandas as pd
import time

#read in the data
while(True):
    try:
        date = input('Enter the date of the games you want to see (MM-DD-YYYY): ')
        if(date == 't' or date == 'today' or date == 'T' or date == 'Today' or date == 'TODAY'):
            date = time.strftime('%m-%d-%Y')
        if(date == 'y' or date == 'yesterday' or date == 'Y' or date == 'Yesterday' or date == 'YESTERDAY'):
            date = time.strftime('%m-%d-%Y', time.localtime(time.time() - 86400))
        path = 'predictions-2025/predictions' + date + '.csv'
        todayTeams = pd.read_csv(path)
        break
    except:
        print('No predictions for that date. Try again.')
        continue
    

print()
print('O/U Predictions:')
print()

for index, row in todayTeams.iterrows():
    if row['PickedTotal'] == 1:
        print('*****  ', end = '')
    if row['TotalPredictions'] > row['Line']:
        print(row['AwayTeam'] + ' @ ' + row['HomeTeam'] + ' (' + (str)(row['Line']) + '): ' + 'OVER BY', (str)(row['TotalPredictions'] - row['Line']), end = '')
    else:
        print(row['AwayTeam'] + ' @ ' + row['HomeTeam'] + ' (' + (str)(row['Line']) + '): ' +  'UNDER BY ', (str)(row['Line'] - row['TotalPredictions']), end = '')
    if row['PickedTotal'] == 1:
        print('  *****', end = '')
    print()
    

#same for the spread, but 5 point threshold
print()
print('Spread Predictions:')
print()

for index, row in todayTeams.iterrows():
    if row['PickedSpread'] == 1:
        print('*****  ', end = '')
    if row['SpreadPredictions'] > row['Spread']:
        if(row['Spread'] > 0):
            print(row['AwayTeam'] + ' @ ' + row['HomeTeam'] + ' ('+ row['HomeTeam'] + ' -' + (str)(row['Spread']) + '): ' + row['HomeTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])), end = '')
        else:
            print(row['AwayTeam'] + ' @ ' + row['HomeTeam'] + ' ('+ row['AwayTeam'] + ' ' + (str)(row['Spread']) + '): ' + row['HomeTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])), end = '')
    else:
        if(row['Spread'] > 0):
            print(row['AwayTeam'] + ' @ ' + row['HomeTeam'] + ' ('+ row['HomeTeam'] + ' -' + (str)(row['Spread']) + '): ' + row['AwayTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])), end = '')
        else:
            print(row['AwayTeam'] + ' @ ' + row['HomeTeam'] + ' ('+ row['AwayTeam'] + ' ' + (str)(row['Spread']) + '): '  + row['AwayTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])), end = '')
    if row['PickedSpread'] == 1:
        print('  *****', end = '')
    print()