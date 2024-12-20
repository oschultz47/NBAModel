import pandas as pd
import time
import sys

def nameToCity(df):
    team_to_city = {
        'Atlanta Hawks': 'Atlanta',
        'Boston Celtics': 'Boston',
        'Brooklyn Nets': 'Brooklyn',
        'Charlotte Hornets': 'Charlotte',
        'Chicago Bulls': 'Chicago',
        'Cleveland Cavaliers': 'Cleveland',
        'Dallas Mavericks': 'Dallas',
        'Denver Nuggets': 'Denver',
        'Detroit Pistons': 'Detroit',
        'Golden State Warriors': 'Golden State',
        'Houston Rockets': 'Houston',
        'Indiana Pacers': 'Indiana',
        'Los Angeles Clippers': 'LA Clippers',
        'Los Angeles Lakers': 'LA Lakers',
        'Memphis Grizzlies': 'Memphis',
        'Miami Heat': 'Miami',
        'Milwaukee Bucks': 'Milwaukee',
        'Minnesota Timberwolves': 'Minnesota',
        'New Orleans Pelicans': 'New Orleans',
        'New York Knicks': 'New York',
        'Oklahoma City Thunder': 'Okla City',
        'Orlando Magic': 'Orlando',
        'Philadelphia 76ers': 'Philadelphia',
        'Phoenix Suns': 'Phoenix',
        'Portland Trail Blazers': 'Portland',
        'Sacramento Kings': 'Sacramento',
        'San Antonio Spurs': 'San Antonio',
        'Toronto Raptors': 'Toronto',
        'Utah Jazz': 'Utah',
        'Washington Wizards': 'Washington'
    }

    df.replace({'Visitor/Neutral': team_to_city, 'Home/Neutral': team_to_city}, inplace=True)
    
    return df

# read in all the data from the csv files in the predictions folder
# and store them in one dataframe
df = pd.DataFrame()

scoresOct = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_games.html')[0]
scoresNov = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_games-november.html')[0]
scoresDec = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_games-december.html')[0]
scoresJan = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_games-january.html')[0]
scoresFeb = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_games-february.html')[0]
scoresMar = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_games-march.html')[0]
scoresApr = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_games-april.html')[0]

scoresOct.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresNov.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresDec.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresJan.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresFeb.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresMar.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresApr.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)

scores = pd.concat([scoresOct, scoresNov, scoresDec, scoresJan, scoresFeb, scoresMar, scoresApr], ignore_index=True)

nameToCity(scores)

scores['Date'] = pd.to_datetime(scores['Date'])
#convert date to string in 01-01-2020 format
scores['Date'] = scores['Date'].dt.strftime('%m-%d-%Y')

saveFile = False

#print(scores.head())
while 1:
    try:
        date = input('Enter the date of the games you want to see (MM-DD-YYYY): ')
        if(date == 'f' or date == 'F' or date == 'FILE' or date == 'file' or date == 'File'):
            print('Printing results to predictionAccuracy-2025.txt...')
            sys.stdout = open('predictionAccuracy-2025.txt', 'w')
        if(date == '' or date == 'a' or date == 'all' or date == 'A' or date == 'All' or date == 'ALL' or date == 'f' or date == 'F' or date == 'FILE' or date == 'file' or date == 'File'):
            # create a list of every file in the predictions folder
            # and store the names in a list
            import os
            path = 'predictions-2025/'
            files = os.listdir(path)

            # loop through the list of files and read them into a dataframe
            # then append the dataframe to the main dataframe

            tempdf = pd.DataFrame()

            for file in files:
                tempdf = pd.read_csv(path + file)
                df = pd.concat([df, tempdf], ignore_index=True)
            #print(df.head())

            # drop all rows where the date is today or in the future
            import datetime
            today = datetime.datetime.today().strftime('%m-%d-%Y')
            df = df[df['Date'] < today]
            if(date == '' or date == 'a' or date == 'all' or date == 'A' or date == 'All' or date == 'ALL'):
                print()
            print('Prediction results from all games:')
            print()
        elif(date == 'y' or date == 'yesterday' or date == 'Y' or date == 'Yesterday' or date == 'YESTERDAY'):
            date = time.strftime('%m-%d-%Y', time.localtime(time.time() - 86400))
            path = 'predictions-2025/predictions' + date + '.csv'
            df = pd.read_csv(path)
            print()
            print('Prediction results from', (str)(date) + ':')
            print()
        else:
            path = 'predictions-2025/predictions' + date + '.csv'
            df = pd.read_csv(path)
            print()
            print('Prediction results from', (str)(date) + ':')
            print()
        break
    except:
        print('No predictions for', date, '. Try again.')
        continue


actualSpread = 0
actualTotal = 0

totalsCorrect = 0
spreadsCorrect = 0
allTotalsCorrect = 0
allSpreadsCorrect = 0
winnersCorrect = 0

totalPredictionsCount = 0
spreadPredictionsCount = 0

# if you only want to see the results of the model's picks over some threshold
totalOffset = 0
spreadOffset = 0

for index, row in df.iterrows():
    #find the actual spread and total for the game
    actualSpread = scores.loc[(scores['Date'] == row['Date']) & (scores['Visitor/Neutral'] == row['AwayTeam']) & (scores['Home/Neutral'] == row['HomeTeam'])]['PTS.1'].values[0] - scores.loc[(scores['Date'] == row['Date']) & (scores['Visitor/Neutral'] == row['AwayTeam']) & (scores['Home/Neutral'] == row['HomeTeam'])]['PTS'].values[0]
    actualTotal = scores.loc[(scores['Date'] == row['Date']) & (scores['Visitor/Neutral'] == row['AwayTeam']) & (scores['Home/Neutral'] == row['HomeTeam'])]['PTS'].values[0] + scores.loc[(scores['Date'] == row['Date']) & (scores['Visitor/Neutral'] == row['AwayTeam']) & (scores['Home/Neutral'] == row['HomeTeam'])]['PTS.1'].values[0]
    if row['TotalPredictions'] > (row['Line'] + totalOffset):
        totalPredictionsCount += 1
        if actualTotal > row['Line']:
            allTotalsCorrect += 1
            if row['PickedTotal'] == 1:
                totalsCorrect += 1
    elif row['TotalPredictions'] < (row['Line'] - totalOffset):
        totalPredictionsCount += 1
        if actualTotal < row['Line']:
            allTotalsCorrect += 1
            if row['PickedTotal'] == 1:
                totalsCorrect += 1
    if (row['SpreadPredictions'] > row['Spread'] + spreadOffset):
        spreadPredictionsCount += 1
        if actualSpread > row['Spread']:
            allSpreadsCorrect += 1
            if row['PickedSpread'] == 1:
                spreadsCorrect += 1
    elif (row['SpreadPredictions'] < row['Spread'] - spreadOffset):
        spreadPredictionsCount += 1
        if actualSpread < row['Spread']:
            allSpreadsCorrect += 1
            if row['PickedSpread'] == 1:
                spreadsCorrect += 1

    if(row['SpreadPredictions'] * actualSpread > 0):
        winnersCorrect += 1

#truncate decimals after 2 places

if len(df) == 0:
    print("The model doesn't have any predictions for that time frame.")
else:

    print("The model predicted", allTotalsCorrect, "out of", totalPredictionsCount, "totals correctly, or", (str)((int)(allTotalsCorrect / totalPredictionsCount * 10000)/100) + "%")
    print("The model predicted", allSpreadsCorrect, "out of", spreadPredictionsCount, "spreads correctly, or", (str)((int)(allSpreadsCorrect / spreadPredictionsCount * 10000)/100) + "%")
    print("The model predicted", winnersCorrect, "out of", len(df), "winners correctly, or", (str)((int)(winnersCorrect / len(df) * 10000)/100) + "%")

    print()

    print("The model predicted", allTotalsCorrect + allSpreadsCorrect, "out of", len(df) * 2, "picks correctly, or", (str)((int)((allTotalsCorrect + allSpreadsCorrect) / (len(df) * 2) * 10000)/ 100) + "%")


    sumTotalsPicked = sum(df['PickedTotal'])
    sumSpreadsPicked = sum(df['PickedSpread'])
    print()
    if sumTotalsPicked == 0:
        print("The model didn't have any \"confident\" totals picks in that time frame.")
    else:
        print("On picks where the model differed from the total by 7 or more points, the model predicted", totalsCorrect, "out of", sumTotalsPicked, "totals correctly, or", (str)((int)(totalsCorrect / sumTotalsPicked * 10000)/100) + "%")
    if sumSpreadsPicked == 0:
        print("The model didn't have any \"confident\" spreads picks in that time frame.")
    else:
        print("On picks where the model differed from the spread by 5 or more points, the model predicted", spreadsCorrect, "out of", sumSpreadsPicked, "spreads correctly, or", (str)((int)(spreadsCorrect / sumSpreadsPicked * 10000)/100) + "%")

    print()

    print("On picks where the model was \"confident\" it picked", totalsCorrect + spreadsCorrect, "out of", sumTotalsPicked + sumSpreadsPicked, "picks correctly, or", (str)((int)((totalsCorrect + spreadsCorrect) / (sumTotalsPicked + sumSpreadsPicked) * 10000)/100) + "%")

    if(date == 'f' or date == 'F' or date == 'FILE' or date == 'file' or date == 'File'):
            sys.stdout = sys.__stdout__
            print('Complete.')