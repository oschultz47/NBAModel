# NBA O/U and Spread Model

`NBAModel` is a model for predicting NBA totals and spreads based on team statistics from [teamrankings.com/nba](https://www.teamrankings.com/nba) and previous game results

# Getting Started

## Required Programs

`NBAModel` requires Python 3.7+ along with the 'pandas' and 'keras' libraries

## Usage

`model.py` is used to compile the models and generate predictions for today's games  
  
`predictionCheck.py` checks the accuracy of the model's predictions on a certain date (or input 'all' to check all of the model's predictions)
  
`printPrediction.py` outputs the model's predictions for a certain date in a readable format  

# Folders and Additional Files

The `predictions` folder contains relevant information about the predictions made by the model so far  
  
The `models` folder contains the most recent version of the models

`predictionAccuracy.txt` contains the accuracy of all of the model's predictions so far