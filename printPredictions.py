import pandas as pd
import time

#read in the data
while(True):
    try:
        date = input('Enter the date of the games you want to see (MM-DD-YYYY): ')
        if(date == 't'):
            date = time.strftime('%m-%d-%Y')
        if(date == 'y'):
            date = time.strftime('%m-%d-%Y', time.localtime(time.time() - 86400))
        path = 'predictions/predictions' + date + '.csv'
        todayTeams = pd.read_csv(path)
        break
    except:
        print('No predictions for that date. Try again.')
        continue
    

print()
print('O/U Predictions:')
print()

for index, row in todayTeams.iterrows():
    if row['TotalPredictions'] > row['Line']:
        print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' (' + (str)(row['Line']) + '): ' + 'OVER BY', (str)(row['TotalPredictions'] - row['Line']))
    elif row['TotalPredictions'] < row['Line']:
        print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' (' + (str)(row['Line']) + '): ' +  'UNDER BY ', (str)(row['Line'] - row['TotalPredictions']))
    else:
        continue

#same for the spread, but 5 point threshold
print()
print('Spread Predictions:')
print()

for index, row in todayTeams.iterrows():
    if row['SpreadPredictions'] > row['Spread']:
        if(row['Spread'] > 0):
            print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' ('+ row['HomeTeam'] + ' -' + (str)(row['Spread']) + '): ' + row['AwayTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])))
        else:
            print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' ('+ row['AwayTeam'] + ' ' + (str)(row['Spread']) + '): ' + row['HomeTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])))
    elif row['SpreadPredictions'] < row['Spread']:
        if(row['Spread'] > 0):
            print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' ('+ row['HomeTeam'] + ' -' + (str)(row['Spread']) + '): ' + row['AwayTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])))
        else:
            print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' ('+ row['AwayTeam'] + ' ' + (str)(row['Spread']) + '): '  + row['HomeTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])))
    else:
        continue