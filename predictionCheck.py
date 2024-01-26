import pandas as pd
import time

# read in all the data from the csv files in the predictions folder
# and store them in one dataframe
df = pd.DataFrame()

scoresOct = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2024_games.html')[0]
scoresNov = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2024_games-november.html')[0]
scoresDec = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2024_games-december.html')[0]
scoresJan = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2024_games-january.html')[0]
scoresFeb = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2024_games-february.html')[0]
scoresMar = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2024_games-march.html')[0]
scoresApr = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2024_games-april.html')[0]

scoresOct.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresNov.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresDec.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresJan.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresFeb.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresMar.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)
scoresApr.drop(['Start (ET)', 'Unnamed: 6', 'Unnamed: 7', 'Attend.', 'Notes', 'Arena'], axis=1, inplace=True)

scores = pd.concat([scoresOct, scoresNov, scoresDec, scoresJan, scoresFeb, scoresMar, scoresApr], ignore_index=True)

scores['Visitor/Neutral'].replace('Atlanta Hawks', 'Atlanta', inplace=True)
scores['Home/Neutral'].replace('Atlanta Hawks', 'Atlanta', inplace=True)
scores['Visitor/Neutral'].replace('Boston Celtics', 'Boston', inplace=True)
scores['Home/Neutral'].replace('Boston Celtics', 'Boston', inplace=True)
scores['Visitor/Neutral'].replace('Brooklyn Nets', 'Brooklyn', inplace=True)
scores['Home/Neutral'].replace('Brooklyn Nets', 'Brooklyn', inplace=True)
scores['Visitor/Neutral'].replace('Charlotte Hornets', 'Charlotte', inplace=True)
scores['Home/Neutral'].replace('Charlotte Hornets', 'Charlotte', inplace=True)
scores['Visitor/Neutral'].replace('Chicago Bulls', 'Chicago', inplace=True)
scores['Home/Neutral'].replace('Chicago Bulls', 'Chicago', inplace=True)
scores['Visitor/Neutral'].replace('Cleveland Cavaliers', 'Cleveland', inplace=True)
scores['Home/Neutral'].replace('Cleveland Cavaliers', 'Cleveland', inplace=True)
scores['Visitor/Neutral'].replace('Dallas Mavericks', 'Dallas', inplace=True)
scores['Home/Neutral'].replace('Dallas Mavericks', 'Dallas', inplace=True)
scores['Visitor/Neutral'].replace('Denver Nuggets', 'Denver', inplace=True)
scores['Home/Neutral'].replace('Denver Nuggets', 'Denver', inplace=True)
scores['Visitor/Neutral'].replace('Detroit Pistons', 'Detroit', inplace=True)
scores['Home/Neutral'].replace('Detroit Pistons', 'Detroit', inplace=True)
scores['Visitor/Neutral'].replace('Golden State Warriors', 'Golden State', inplace=True)
scores['Home/Neutral'].replace('Golden State Warriors', 'Golden State', inplace=True)
scores['Visitor/Neutral'].replace('Houston Rockets', 'Houston', inplace=True)
scores['Home/Neutral'].replace('Houston Rockets', 'Houston', inplace=True)
scores['Visitor/Neutral'].replace('Indiana Pacers', 'Indiana', inplace=True)
scores['Home/Neutral'].replace('Indiana Pacers', 'Indiana', inplace=True)
scores['Visitor/Neutral'].replace('Los Angeles Clippers', 'LA Clippers', inplace=True)
scores['Home/Neutral'].replace('Los Angeles Clippers', 'LA Clippers', inplace=True)
scores['Visitor/Neutral'].replace('Los Angeles Lakers', 'LA Lakers', inplace=True)
scores['Home/Neutral'].replace('Los Angeles Lakers', 'LA Lakers', inplace=True)
scores['Visitor/Neutral'].replace('Memphis Grizzlies', 'Memphis', inplace=True) 
scores['Home/Neutral'].replace('Memphis Grizzlies', 'Memphis', inplace=True)
scores['Visitor/Neutral'].replace('Miami Heat', 'Miami', inplace=True)
scores['Home/Neutral'].replace('Miami Heat', 'Miami', inplace=True)
scores['Visitor/Neutral'].replace('Milwaukee Bucks', 'Milwaukee', inplace=True)
scores['Home/Neutral'].replace('Milwaukee Bucks', 'Milwaukee', inplace=True)
scores['Visitor/Neutral'].replace('Minnesota Timberwolves', 'Minnesota', inplace=True)
scores['Home/Neutral'].replace('Minnesota Timberwolves', 'Minnesota', inplace=True)
scores['Visitor/Neutral'].replace('New Orleans Pelicans', 'New Orleans', inplace=True)
scores['Home/Neutral'].replace('New Orleans Pelicans', 'New Orleans', inplace=True)
scores['Visitor/Neutral'].replace('New York Knicks', 'New York', inplace=True)
scores['Home/Neutral'].replace('New York Knicks', 'New York', inplace=True)
scores['Visitor/Neutral'].replace('Oklahoma City Thunder', 'Okla City', inplace=True)
scores['Home/Neutral'].replace('Oklahoma City Thunder', 'Okla City', inplace=True)
scores['Visitor/Neutral'].replace('Orlando Magic', 'Orlando', inplace=True)
scores['Home/Neutral'].replace('Orlando Magic', 'Orlando', inplace=True)
scores['Visitor/Neutral'].replace('Philadelphia 76ers', 'Philadelphia', inplace=True)
scores['Home/Neutral'].replace('Philadelphia 76ers', 'Philadelphia', inplace=True)
scores['Visitor/Neutral'].replace('Phoenix Suns', 'Phoenix', inplace=True)
scores['Home/Neutral'].replace('Phoenix Suns', 'Phoenix', inplace=True)
scores['Visitor/Neutral'].replace('Portland Trail Blazers', 'Portland', inplace=True)
scores['Home/Neutral'].replace('Portland Trail Blazers', 'Portland', inplace=True)
scores['Visitor/Neutral'].replace('Sacramento Kings', 'Sacramento', inplace=True)
scores['Home/Neutral'].replace('Sacramento Kings', 'Sacramento', inplace=True)
scores['Visitor/Neutral'].replace('San Antonio Spurs', 'San Antonio', inplace=True)
scores['Home/Neutral'].replace('San Antonio Spurs', 'San Antonio', inplace=True)
scores['Visitor/Neutral'].replace('Toronto Raptors', 'Toronto', inplace=True)
scores['Home/Neutral'].replace('Toronto Raptors', 'Toronto', inplace=True)
scores['Visitor/Neutral'].replace('Utah Jazz', 'Utah', inplace=True)
scores['Home/Neutral'].replace('Utah Jazz', 'Utah', inplace=True)
scores['Visitor/Neutral'].replace('Washington Wizards', 'Washington', inplace=True)
scores['Home/Neutral'].replace('Washington Wizards', 'Washington', inplace=True)

scores['Date'] = pd.to_datetime(scores['Date'])
#convert date to string in 01-01-2020 format
scores['Date'] = scores['Date'].dt.strftime('%m-%d-%Y')

#print(scores.head())
while 1:
    try:
        date = input('Enter the date of the games you want to see (MM-DD-YYYY): ')

        if(date == '' or date == 'a' or date == 'all' or date == 'A' or date == 'All' or date == 'ALL'):
            # create a list of every file in the predictions folder
            # and store the names in a list
            import os
            path = 'predictions/'
            files = os.listdir(path)

            # loop through the list of files and read them into a dataframe
            # then append the dataframe to the main dataframe

            tempdf = pd.DataFrame()

            for file in files:
                tempdf = pd.read_csv(path + file)
                df = df.append(tempdf, ignore_index=True)

            #print(df.head())

            # drop all rows where the date is today or in the future
            import datetime
            today = datetime.datetime.today().strftime('%m-%d-%Y')
            df = df[df['Date'] < today]
            print()
            print('Prediction results from all games:')
            print()
            break
        elif(date == 'y' or date == 'yesterday' or date == 'Y' or date == 'Yesterday' or date == 'YESTERDAY'):
            date = time.strftime('%m-%d-%Y', time.localtime(time.time() - 86400))
            path = 'predictions/predictions' + date + '.csv'
            df = pd.read_csv(path)
            print()
            print('Prediction results from', (str)(date) + ':')
            print()
            break
        else:
            path = 'predictions/predictions' + date + '.csv'
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

for index, row in df.iterrows():
    #find the actual spread and total for the game
    actualSpread = scores.loc[(scores['Date'] == row['Date']) & (scores['Visitor/Neutral'] == row['AwayTeam']) & (scores['Home/Neutral'] == row['HomeTeam'])]['PTS.1'].values[0] - scores.loc[(scores['Date'] == row['Date']) & (scores['Visitor/Neutral'] == row['AwayTeam']) & (scores['Home/Neutral'] == row['HomeTeam'])]['PTS'].values[0]
    actualTotal = scores.loc[(scores['Date'] == row['Date']) & (scores['Visitor/Neutral'] == row['AwayTeam']) & (scores['Home/Neutral'] == row['HomeTeam'])]['PTS'].values[0] + scores.loc[(scores['Date'] == row['Date']) & (scores['Visitor/Neutral'] == row['AwayTeam']) & (scores['Home/Neutral'] == row['HomeTeam'])]['PTS.1'].values[0]
    if row['TotalPredictions'] > row['Line']:
        if actualTotal > row['Line']:
            allTotalsCorrect += 1
            if row['PickedTotal'] == 1:
                totalsCorrect += 1
    else:
        if actualTotal < row['Line']:
            allTotalsCorrect += 1
            if row['PickedTotal'] == 1:
                totalsCorrect += 1
    if (row['SpreadPredictions'] > row['Spread']):
        if actualSpread > row['Spread']:
            allSpreadsCorrect += 1
            if row['PickedSpread'] == 1:
                spreadsCorrect += 1
    else:
        if actualSpread < row['Spread']:
            allSpreadsCorrect += 1
            print(row['HomeTeam'])
            if row['PickedSpread'] == 1:
                spreadsCorrect += 1

#truncate decimals after 2 places

if len(df) == 0:
    print("No games have been predicted yet (or they're all in the future)")
else:

    print("The model predicted", allTotalsCorrect, "out of", len(df), "totals correctly, or", (str)((int)(allTotalsCorrect / len(df) * 10000)/100) + "%")
    print("The model predicted", allSpreadsCorrect, "out of", len(df), "spreads correctly, or", (str)((int)(allSpreadsCorrect / len(df) * 10000)/100) + "%")

    print()

    print("The model predicted", allTotalsCorrect + allSpreadsCorrect, "out of", len(df) * 2, "picks correctly, or", (str)((int)((allTotalsCorrect + allSpreadsCorrect) / (len(df) * 2) * 10000)/ 100) + "%")


    sumTotalsPicked = sum(df['PickedTotal'])
    sumSpreadsPicked = sum(df['PickedSpread'])
    print()

    print("On picks where the model differed from the total by 7 or more points, the model predicted", totalsCorrect, "out of", sumTotalsPicked, "totals correctly, or", (str)((int)(totalsCorrect / sumTotalsPicked * 10000)/100) + "%")
    print("On picks where the model differed from the spread by 5 or more points, the model predicted", spreadsCorrect, "out of", sumSpreadsPicked, "spreads correctly, or", (str)((int)(spreadsCorrect / sumSpreadsPicked * 10000)/100) + "%")

    print()

    print("On picks where the model was \"confident\" it picked", totalsCorrect + spreadsCorrect, "out of", sumTotalsPicked + sumSpreadsPicked, "picks correctly, or", (str)((int)((totalsCorrect + spreadsCorrect) / (sumTotalsPicked + sumSpreadsPicked) * 10000)/100) + "%")