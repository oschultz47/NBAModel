import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

games = pd.read_csv('games.csv')
spreads = pd.read_csv('spreads.csv')
totals = pd.read_csv('totals.csv')

games = games.drop(columns=['Date', 'HomeTeam', 'AwayTeam'])

print(games.head())
print(spreads.head())
print(totals.head())

from sklearn.model_selection import train_test_split

X = games
y = totals['Total']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

model = LinearRegression()
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

print(mean_squared_error(y_test, predictions))
print(r2_score(y_test, predictions))

coef_df = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_})
print(coef_df.sort_values(by='Coefficient', ascending=False))

# save the model to csv
coef_df.to_csv('model.csv', index=False)

#drop the features from games with absolute coefficient less than 1
low_coef = coef_df[abs(coef_df['Coefficient']) < 3]
games = games.drop(columns=low_coef['Feature'])
print(games.head())

X = games
y = totals['Total']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(mean_squared_error(y_test, predictions))
print(r2_score(y_test, predictions))