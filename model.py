import pandas as pd
#from sklearn.linear_model import LinearRegression

from keras.models import Sequential
from keras.layers import Dense

from keras.models import load_model

import datetime
import os.path

def nameToCity(df):
    df['Visitor/Neutral'].replace('Atlanta Hawks', 'Atlanta', inplace=True)
    df['Home/Neutral'].replace('Atlanta Hawks', 'Atlanta', inplace=True)
    df['Visitor/Neutral'].replace('Boston Celtics', 'Boston', inplace=True)
    df['Home/Neutral'].replace('Boston Celtics', 'Boston', inplace=True)
    df['Visitor/Neutral'].replace('Brooklyn Nets', 'Brooklyn', inplace=True)
    df['Home/Neutral'].replace('Brooklyn Nets', 'Brooklyn', inplace=True)
    df['Visitor/Neutral'].replace('Charlotte Hornets', 'Charlotte', inplace=True)
    df['Home/Neutral'].replace('Charlotte Hornets', 'Charlotte', inplace=True)
    df['Visitor/Neutral'].replace('Chicago Bulls', 'Chicago', inplace=True)
    df['Home/Neutral'].replace('Chicago Bulls', 'Chicago', inplace=True)
    df['Visitor/Neutral'].replace('Cleveland Cavaliers', 'Cleveland', inplace=True)
    df['Home/Neutral'].replace('Cleveland Cavaliers', 'Cleveland', inplace=True)
    df['Visitor/Neutral'].replace('Dallas Mavericks', 'Dallas', inplace=True)
    df['Home/Neutral'].replace('Dallas Mavericks', 'Dallas', inplace=True)
    df['Visitor/Neutral'].replace('Denver Nuggets', 'Denver', inplace=True)
    df['Home/Neutral'].replace('Denver Nuggets', 'Denver', inplace=True)
    df['Visitor/Neutral'].replace('Detroit Pistons', 'Detroit', inplace=True)
    df['Home/Neutral'].replace('Detroit Pistons', 'Detroit', inplace=True)
    df['Visitor/Neutral'].replace('Golden State Warriors', 'Golden State', inplace=True)
    df['Home/Neutral'].replace('Golden State Warriors', 'Golden State', inplace=True)
    df['Visitor/Neutral'].replace('Houston Rockets', 'Houston', inplace=True)
    df['Home/Neutral'].replace('Houston Rockets', 'Houston', inplace=True)
    df['Visitor/Neutral'].replace('Indiana Pacers', 'Indiana', inplace=True)
    df['Home/Neutral'].replace('Indiana Pacers', 'Indiana', inplace=True)
    df['Visitor/Neutral'].replace('Los Angeles Clippers', 'LA Clippers', inplace=True)
    df['Home/Neutral'].replace('Los Angeles Clippers', 'LA Clippers', inplace=True)
    df['Visitor/Neutral'].replace('Los Angeles Lakers', 'LA Lakers', inplace=True)
    df['Home/Neutral'].replace('Los Angeles Lakers', 'LA Lakers', inplace=True)
    df['Visitor/Neutral'].replace('Memphis Grizzlies', 'Memphis', inplace=True) 
    df['Home/Neutral'].replace('Memphis Grizzlies', 'Memphis', inplace=True)
    df['Visitor/Neutral'].replace('Miami Heat', 'Miami', inplace=True)
    df['Home/Neutral'].replace('Miami Heat', 'Miami', inplace=True)
    df['Visitor/Neutral'].replace('Milwaukee Bucks', 'Milwaukee', inplace=True)
    df['Home/Neutral'].replace('Milwaukee Bucks', 'Milwaukee', inplace=True)
    df['Visitor/Neutral'].replace('Minnesota Timberwolves', 'Minnesota', inplace=True)
    df['Home/Neutral'].replace('Minnesota Timberwolves', 'Minnesota', inplace=True)
    df['Visitor/Neutral'].replace('New Orleans Pelicans', 'New Orleans', inplace=True)
    df['Home/Neutral'].replace('New Orleans Pelicans', 'New Orleans', inplace=True)
    df['Visitor/Neutral'].replace('New York Knicks', 'New York', inplace=True)
    df['Home/Neutral'].replace('New York Knicks', 'New York', inplace=True)
    df['Visitor/Neutral'].replace('Oklahoma City Thunder', 'Okla City', inplace=True)
    df['Home/Neutral'].replace('Oklahoma City Thunder', 'Okla City', inplace=True)
    df['Visitor/Neutral'].replace('Orlando Magic', 'Orlando', inplace=True)
    df['Home/Neutral'].replace('Orlando Magic', 'Orlando', inplace=True)
    df['Visitor/Neutral'].replace('Philadelphia 76ers', 'Philadelphia', inplace=True)
    df['Home/Neutral'].replace('Philadelphia 76ers', 'Philadelphia', inplace=True)
    df['Visitor/Neutral'].replace('Phoenix Suns', 'Phoenix', inplace=True)
    df['Home/Neutral'].replace('Phoenix Suns', 'Phoenix', inplace=True)
    df['Visitor/Neutral'].replace('Portland Trail Blazers', 'Portland', inplace=True)
    df['Home/Neutral'].replace('Portland Trail Blazers', 'Portland', inplace=True)
    df['Visitor/Neutral'].replace('Sacramento Kings', 'Sacramento', inplace=True)
    df['Home/Neutral'].replace('Sacramento Kings', 'Sacramento', inplace=True)
    df['Visitor/Neutral'].replace('San Antonio Spurs', 'San Antonio', inplace=True)
    df['Home/Neutral'].replace('San Antonio Spurs', 'San Antonio', inplace=True)
    df['Visitor/Neutral'].replace('Toronto Raptors', 'Toronto', inplace=True)
    df['Home/Neutral'].replace('Toronto Raptors', 'Toronto', inplace=True)
    df['Visitor/Neutral'].replace('Utah Jazz', 'Utah', inplace=True)
    df['Home/Neutral'].replace('Utah Jazz', 'Utah', inplace=True)
    df['Visitor/Neutral'].replace('Washington Wizards', 'Washington', inplace=True)
    df['Home/Neutral'].replace('Washington Wizards', 'Washington', inplace=True)
    return df

lines = pd.DataFrame()

i=0
temp = 0
while 1:
    try:
        gameLine = pd.read_html('https://www.espn.com/nba/lines/_/date')[i]
        gameLine.columns = ['TEAM', 'REC', 'LINE', 'ML', 'BPI']
        lines.loc[i, 'Home/Neutral'] = gameLine.loc[1, 'TEAM']
        lines.loc[i, 'Visitor/Neutral'] = gameLine.loc[0, 'TEAM']
        lines.loc[i, 'Line'] = gameLine.loc[0, 'LINE']
        lines.loc[i, 'Spread'] = -1 * (gameLine.loc[1, 'LINE'])
        if(lines.loc[i, 'Line'] < 100):
            lines.loc[i, 'Line'] = gameLine.loc[1, 'LINE']
            lines.loc[i, 'Spread'] = gameLine.loc[0, 'LINE']
        i = i + 1
    except:
        break

ppg = pd.read_html('https://www.teamrankings.com/nba/stat/points-per-game')[0]
oe = pd.read_html('https://www.teamrankings.com/nba/stat/offensive-efficiency')[0]
pip = pd.read_html('https://www.teamrankings.com/nba/stat/points-in-paint-per-game')[0]
fbp = pd.read_html('https://www.teamrankings.com/nba/stat/fastbreak-points-per-game')[0]
tp = pd.read_html('https://www.teamrankings.com/nba/stat/three-point-pct')[0]
ftp = pd.read_html('https://www.teamrankings.com/nba/stat/free-throw-pct')[0]
trb = pd.read_html('https://www.teamrankings.com/nba/stat/total-rebounds-per-game')[0]
fpg = pd.read_html('https://www.teamrankings.com/nba/stat/personal-fouls-per-game')[0]
oppg = pd.read_html('https://www.teamrankings.com/nba/stat/opponent-points-per-game')[0]
de = pd.read_html('https://www.teamrankings.com/nba/stat/defensive-efficiency')[0]
opip = pd.read_html('https://www.teamrankings.com/nba/stat/opponent-points-in-paint-per-game')[0]
ofbp = pd.read_html('https://www.teamrankings.com/nba/stat/opponent-fastbreak-points-per-game')[0]
otp = pd.read_html('https://www.teamrankings.com/nba/stat/opponent-three-point-pct')[0]
otrb = pd.read_html('https://www.teamrankings.com/nba/stat/opponent-total-rebounds-per-game')[0]
ofpg = pd.read_html('https://www.teamrankings.com/nba/stat/opponent-personal-fouls-per-game')[0]
possesions = pd.read_html('https://www.teamrankings.com/nba/stat/possessions-per-game')[0]
epr = pd.read_html('https://www.teamrankings.com/nba/stat/effective-possession-ratio')[0]
oepr = pd.read_html('https://www.teamrankings.com/nba/stat/opponent-effective-possession-ratio')[0]

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

ppg.drop(['Rank', '2023'], axis=1, inplace=True)
oe.drop(['Rank', '2023'], axis=1, inplace=True)
pip.drop(['Rank', '2023'], axis=1, inplace=True)
fbp.drop(['Rank', '2023'], axis=1, inplace=True)
tp.drop(['Rank', '2023'], axis=1, inplace=True)
ftp.drop(['Rank', '2023'], axis=1, inplace=True)
trb.drop(['Rank', '2023'], axis=1, inplace=True)
fpg.drop(['Rank', '2023'], axis=1, inplace=True)
oppg.drop(['Rank', '2023'], axis=1, inplace=True)
de.drop(['Rank', '2023'], axis=1, inplace=True)
opip.drop(['Rank', '2023'], axis=1, inplace=True)
ofbp.drop(['Rank', '2023'], axis=1, inplace=True)
otp.drop(['Rank', '2023'], axis=1, inplace=True)
otrb.drop(['Rank', '2023'], axis=1, inplace=True)
ofpg.drop(['Rank', '2023'], axis=1, inplace=True)
possesions.drop(['Rank', '2023'], axis=1, inplace=True)
epr.drop(['Rank', '2023'], axis=1, inplace=True)
oepr.drop(['Rank', '2023'], axis=1, inplace=True)

ppg.columns = ['Team', '2024PPG', 'L3PPG', 'L1PPG', 'HomePPG', 'AwayPPG']
oe.columns = ['Team', '2024OE', 'L3OE', 'L1OE', 'HomeOE', 'AwayOE']
pip.columns = ['Team', '2024PIP', 'L3PIP', 'L1PIP', 'HomePIP', 'AwayPIP']
fbp.columns = ['Team', '2024FBP', 'L3FBP', 'L1FBP', 'HomeFBP', 'AwayFBP']
tp.columns = ['Team', '2024TP', 'L3TP', 'L1TP', 'HomeTP', 'AwayTP']
ftp.columns = ['Team', '2024FTP', 'L3FTP', 'L1FTP', 'HomeFTP', 'AwayFTP']
trb.columns = ['Team', '2024TRB', 'L3TRB', 'L1TRB', 'HomeTRB', 'AwayTRB']
fpg.columns = ['Team', '2024FPG', 'L3FPG', 'L1FPG', 'HomeFPG', 'AwayFPG']
oppg.columns = ['Team', '2024OPPG', 'L3OPPG', 'L1OPPG', 'HomeOPPG', 'AwayOPPG']
de.columns = ['Team', '2024DE', 'L3DE', 'L1DE', 'HomeDE', 'AwayDE']
opip.columns = ['Team', '2024OPIP', 'L3OPIP', 'L1OPIP', 'HomeOPIP', 'AwayOPIP']
ofbp.columns = ['Team', '2024OFBP', 'L3OFBP', 'L1OFBP', 'HomeOFBP', 'AwayOFBP']
otp.columns = ['Team', '2024OTP', 'L3OTP', 'L1OTP', 'HomeOTP', 'AwayOTP']
otrb.columns = ['Team', '2024OTRB', 'L3OTRB', 'L1OTRB', 'HomeOTRB', 'AwayOTRB']
ofpg.columns = ['Team', '2024OFPG', 'L3OFPG', 'L1OFPG', 'HomeOFPG', 'AwayOFPG']
possesions.columns = ['Team', '2024Poss', 'L3Poss', 'L1Poss', 'HomePoss', 'AwayPoss']
epr.columns = ['Team', '2024EPR', 'L3EPR', 'L1EPR', 'HomeEPR', 'AwayEPR']
oepr.columns = ['Team', '2024OEPR', 'L3OEPR', 'L1OEPR', 'HomeOEPR', 'AwayOEPR']

#free throw percentage is a string, convert to float
ftp['2024FTP'] = ftp['2024FTP'].str.replace('%', '').astype(float)
ftp['L3FTP'] = ftp['L3FTP'].str.replace('%', '').astype(float)
ftp['L1FTP'] = ftp['L1FTP'].str.replace('%', '').astype(float)
ftp['HomeFTP'] = ftp['HomeFTP'].str.replace('%', '').astype(float)
ftp['AwayFTP'] = ftp['AwayFTP'].str.replace('%', '').astype(float)

#merge dataframes
df = pd.merge(ppg, oe, on='Team')
df = pd.merge(df, pip, on='Team')
df = pd.merge(df, fbp, on='Team')
df = pd.merge(df, tp, on='Team')
df = pd.merge(df, ftp, on='Team')
df = pd.merge(df, trb, on='Team')
df = pd.merge(df, fpg, on='Team')
df = pd.merge(df, oppg, on='Team')
df = pd.merge(df, de, on='Team')
df = pd.merge(df, opip, on='Team')
df = pd.merge(df, ofbp, on='Team')
df = pd.merge(df, otp, on='Team')
df = pd.merge(df, otrb, on='Team')
df = pd.merge(df, ofpg, on='Team')
df = pd.merge(df, possesions, on='Team')
df = pd.merge(df, epr, on='Team')
df = pd.merge(df, oepr, on='Team')

#merge scores dataframes vertically and reset indexes
scores = pd.concat([scoresOct, scoresNov, scoresDec, scoresJan, scoresFeb, scoresMar, scoresApr], ignore_index=True)

# replace all team names with just the city name in scores dataframes
nameToCity(scores)
nameToCity(lines)

#make a dataframe with just todays games to predict
index = scores[scores['PTS'].isnull()].index[0]
numGames = lines.shape[0]
today = scores.iloc[index:index+numGames, :]
today.reset_index(inplace=True)

scores.dropna(inplace=True)

games = pd.DataFrame()
totals = pd.DataFrame()
spreads = pd.DataFrame()

for index, row in scores.iterrows():
    #add the date and home team from the scores dataframe to the games dataframe
    games = games.append({'Date': row['Date'], 'HomeTeam': row['Home/Neutral'], 'AwayTeam' : row['Visitor/Neutral']}, ignore_index=True)
    #fill in the rest of the stats based on the team name
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomePPG'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomePPG'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeOE'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOE'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomePIP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomePIP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeFBP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeFBP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeTP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeTP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeFTP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeFTP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeTRB'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeTRB'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeFPG'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeFPG'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeOPPG'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOPPG'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeDE'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeDE'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeOPIP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOPIP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeOFBP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOFBP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeOTP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOTP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeOTRB'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOTRB'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeOFPG'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOFPG'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomePoss'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomePoss'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeEPR'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeEPR'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeOEPR'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOEPR'].iloc[0]

    # same for the away team
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayPPG'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayPPG'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayOE'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOE'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayPIP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayPIP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayFBP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayFBP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayTP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayTP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayFTP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayFTP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayTRB'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayTRB'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayFPG'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayFPG'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayOPPG'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOPPG'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayDE'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayDE'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayOPIP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOPIP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayOFBP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOFBP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayOTP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOTP'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayOTRB'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOTRB'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayOFPG'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOFPG'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayPoss'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayPoss'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayEPR'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayEPR'].iloc[0]
    games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayOEPR'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOEPR'].iloc[0]

    #check if the home team played the day before
    if(games.loc[(pd.to_datetime(games['Date']) == (pd.to_datetime(row['Date']) - datetime.timedelta(days=1) )) & ((games['HomeTeam'] == row['Home/Neutral']) | (games['AwayTeam'] == row['Home/Neutral'])), 'HomeTeam'].shape[0] > 0):
        games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeBackToBack'] = 1
    else:
        games.loc[(games['Date'] == row['Date'] ) & (games['HomeTeam'] == row['Home/Neutral']), 'HomeBackToBack'] = 0

    if(games.loc[(pd.to_datetime(games['Date']) == (pd.to_datetime(row['Date']) - datetime.timedelta(days=1) )) & ((games['HomeTeam'] == row['Home/Neutral']) | (games['AwayTeam'] == row['Home/Neutral'])), 'HomeTeam'].shape[0] > 0):
        games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayBackToBack'] = 1
    else:
        games.loc[(games['Date'] == row['Date'] ) & (games['AwayTeam'] == row['Visitor/Neutral']), 'AwayBackToBack'] = 0

    #add the actual game total and the actual game spread to the totals and spreads dataframes
    totals = totals.append({'Total': row['PTS'] + row['PTS.1']}, ignore_index=True)
    spreads = spreads.append({'Spread': row['PTS.1'] - row['PTS']}, ignore_index=True)


#print all the rows in the games dataframe
pd.set_option('display.max_rows', 800)
#print just the Date, HomeTeam, and HomeBackToBack columns
#print(games[['Date', 'HomeTeam', 'HomeBackToBack']])

#convert time of possession and opponent time of possession percentage from string to float
games['HomeTP'] = games['HomeTP'].str.replace('%', '').astype(float)
games['AwayTP'] = games['AwayTP'].str.replace('%', '').astype(float)
games['HomeOTP'] = games['HomeOTP'].str.replace('%', '').astype(float)
games['AwayOTP'] = games['AwayOTP'].str.replace('%', '').astype(float)

#games = games.drop(['Date', 'HomeTeam', 'AwayTeam'], axis=1)

##remove every 10th row from the games dataframe to use as test data
#test = games.iloc[::10, :]
#testTotals = totals.iloc[::10, :]  
#games = games.drop(games.index[::10])
#totals = totals.drop(totals.index[::10])
#testSpreads = spreads.iloc[::10, :]
#spreads = spreads.drop(spreads.index[::10])


#make a model using keras that predicts the total points scored in a game based on the data in the games dataframe

#Set to true to make a new model, false to load an existing model
#if the predictions csv file exists, load the model, otherwise make a new one
modelMake = True
date = datetime.datetime.today().strftime('%m-%d-%Y')
nameString = 'predictions/predictions' + date + '.csv'
if(os.path.exists(nameString)):
    modelMake = False

if(modelMake):
    totalsModel = Sequential()
    totalsModel.add(Dense(64, input_dim=38, activation='relu'))
    totalsModel.add(Dense(64, activation='relu'))
    totalsModel.add(Dense(64, activation='relu'))
    totalsModel.add(Dense(1, activation='linear'))

    totalsModel.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    totalsModel.fit(games.drop(['Date', 'HomeTeam', 'AwayTeam'], axis=1), totals, epochs=300, batch_size=32)

    spreadsModel = Sequential()
    spreadsModel.add(Dense(64, input_dim=38, activation='relu'))
    spreadsModel.add(Dense(64, activation='relu'))
    spreadsModel.add(Dense(64, activation='relu'))
    spreadsModel.add(Dense(1, activation='linear'))

    spreadsModel.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    spreadsModel.fit(games.drop(['Date', 'HomeTeam', 'AwayTeam'], axis=1), spreads, epochs=300, batch_size=32)

    totalsModel.save('models/totalsModel.h5')
    spreadsModel.save('models/spreadsModel.h5')
else:
    totalsModel = load_model('models/totalsModel.h5')
    spreadsModel = load_model('models/spreadsModel.h5')

##test the model using the test data
#PredictedScores = model.predict(test)
#
##test the model using the test data
#PredictedSpreads = model2.predict(test)
#
##make a new dataframe with the predicted scores and actual scores
#predictions = pd.DataFrame()
#predictions['PredictedScore'] = PredictedScores.flatten()
#predictions['ActualScore'] = testTotals.values.flatten()
#predictions['PredictedSpread'] = PredictedSpreads.flatten()
#predictions['ActualSpread'] = testSpreads.values.flatten()
#predictions['DifferenceScore'] = predictions['PredictedScore'] - predictions['ActualScore']
#predictions['DifferenceSpread'] = predictions['PredictedSpread'] - predictions['ActualSpread']
#
#print(predictions.head(100))
#
#correctScore = 0
#correctSpread = 0
#for index, row in predictions.iterrows():
#    if(abs(row['DifferenceScore']) < 10):
#        correctScore = correctScore + 1
#    if(abs(row['DifferenceSpread']) < 5):
#        correctSpread = correctSpread + 1
#
#print('Correct Score: ' + str(correctScore) + ' out of ' + str(predictions.shape[0]))
#print('Correct Score Percentage: ' + str(correctScore/predictions.shape[0]))
#print('Correct Spread: ' + str(correctSpread) + ' out of ' + str(predictions.shape[0]))
#print('Correct Spread Percentage: ' + str(correctSpread/predictions.shape[0]))

todayGames = pd.DataFrame()

for index, row in today.iterrows():
    #add the date and home team from the today dataframe to the games dataframe
    todayGames = todayGames.append({'Date': row['Date'], 'HomeTeam': row['Home/Neutral'], 'AwayTeam' : row['Visitor/Neutral']}, ignore_index=True)
    #fill in the rest of the stats based on the team name
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomePPG'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomePPG'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeOE'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOE'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomePIP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomePIP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeFBP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeFBP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeTP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeTP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeFTP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeFTP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeTRB'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeTRB'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeFPG'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeFPG'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeOPPG'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOPPG'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeDE'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeDE'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeOPIP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOPIP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeOFBP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOFBP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeOTP'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOTP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeOTRB'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOTRB'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeOFPG'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOFPG'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomePoss'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomePoss'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeEPR'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeEPR'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeOEPR'] = df.loc[df['Team'] == row['Home/Neutral'], 'HomeOEPR'].iloc[0]

    # same for the away team
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayPPG'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayPPG'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayOE'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOE'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayPIP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayPIP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayFBP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayFBP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayTP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayTP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayFTP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayFTP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayTRB'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayTRB'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayFPG'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayFPG'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayOPPG'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOPPG'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayDE'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayDE'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayOPIP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOPIP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayOFBP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOFBP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayOTP'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOTP'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayOTRB'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOTRB'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayOFPG'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOFPG'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayPoss'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayPoss'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayEPR'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayEPR'].iloc[0]
    todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayOEPR'] = df.loc[df['Team'] == row['Visitor/Neutral'], 'AwayOEPR'].iloc[0]

     #check if the home team played the day before
    if(games.loc[((pd.to_datetime(games['Date'])) == (pd.to_datetime(row['Date']) - datetime.timedelta(days=1) )) & ((games['HomeTeam'] == row['Home/Neutral']) | (games['AwayTeam'] == row['Home/Neutral'])), 'HomeTeam'].shape[0] > 0):
        todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeBackToBack'] = 1
    else:
        todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['HomeTeam'] == row['Home/Neutral']), 'HomeBackToBack'] = 0

    if(games.loc[(pd.to_datetime(games['Date']) == (pd.to_datetime(row['Date']) - datetime.timedelta(days=1) )) & ((games['HomeTeam'] == row['Home/Neutral']) | (games['AwayTeam'] == row['Home/Neutral'])), 'HomeTeam'].shape[0] > 0):
        todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayBackToBack'] = 1
    else:
        todayGames.loc[(todayGames['Date'] == row['Date'] ) & (todayGames['AwayTeam'] == row['Visitor/Neutral']), 'AwayBackToBack'] = 0

todayGames['HomeTP'] = todayGames['HomeTP'].str.replace('%', '').astype(float)
todayGames['AwayTP'] = todayGames['AwayTP'].str.replace('%', '').astype(float)
todayGames['HomeOTP'] = todayGames['HomeOTP'].str.replace('%', '').astype(float)
todayGames['AwayOTP'] = todayGames['AwayOTP'].str.replace('%', '').astype(float)

todayTeams = todayGames[['HomeTeam', 'AwayTeam']]

todayGames = todayGames.drop(['Date', 'HomeTeam', 'AwayTeam'], axis=1)
totalPredictions = totalsModel.predict(todayGames)
spreadPredictions = spreadsModel.predict(todayGames)  

#add the predictions to the todayTeams dataframe
todayTeams['TotalPredictions'] = totalPredictions
todayTeams['SpreadPredictions'] = spreadPredictions
for index, row in todayTeams.iterrows():
    todayTeams.loc[index, 'Line'] = lines.loc[(lines['Home/Neutral'] == row['HomeTeam']), 'Line'].iloc[0]
    todayTeams.loc[index, 'Spread'] = lines.loc[(lines['Home/Neutral'] == row['HomeTeam']), 'Spread'].iloc[0]

#print the whole todayTeams dataframe
pd.set_option('display.max_rows', 100)
print(todayTeams)

#if the prediction is greater or less than the line by 7 points or more, print the game
print()
print('Bettable O/U Games:')
print()

todayTeams['PickedSpread'] = 0
todayTeams['PickedTotal'] = 0

for index, row in todayTeams.iterrows():
    if row['TotalPredictions'] > row['Line'] + 7:
        print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' (' + (str)(row['Line']) + '): ' + 'OVER BY', (str)(row['TotalPredictions'] - row['Line']))
        todayTeams.loc[index, 'PickedTotal'] += 1
    elif row['TotalPredictions'] < row['Line'] - 7:
        print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' (' + (str)(row['Line']) + '): ' +  'UNDER BY ', (str)(row['Line'] - row['TotalPredictions']))
        todayTeams.loc[index, 'PickedTotal'] += 1
    else:
        continue

#same for the spread, but 5 point threshold
print()
print('Bettable Spread Games:')
print()

for index, row in todayTeams.iterrows():
    if row['SpreadPredictions'] > row['Spread'] + 5:
        if(row['Spread'] > 0):
            print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' ('+ row['HomeTeam'] + ' -' + (str)(row['Spread']) + '): ' + row['HomeTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])))
            todayTeams.loc[index, 'PickedSpread'] += 1
        else:
            print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' ('+ row['AwayTeam'] + ' ' + (str)(row['Spread']) + '): ' + row['HomeTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])))
            todayTeams.loc[index, 'PickedSpread'] += 1
    elif row['SpreadPredictions'] < row['Spread'] - 5:
        if(row['Spread'] > 0):
            print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' ('+ row['HomeTeam'] + ' -' + (str)(row['Spread']) + '): ' + row['AwayTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])))
            todayTeams.loc[index, 'PickedSpread'] += 1
        else:
            print(row['HomeTeam'] + ' @ ' + row['AwayTeam'] + ' ('+ row['AwayTeam'] + ' ' + (str)(row['Spread']) + '): '  + row['AwayTeam'] + ' COVERS BY', (str)(abs(row['Spread'] - row['SpreadPredictions'])))
            todayTeams.loc[index, 'PickedSpread'] += 1
    else:
        continue
print()

# make a csv file with the predictions
todayTeams['Date'] = date
todayTeams.to_csv(nameString, index=False)