# explore data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import datetime
print('main imports done')

df = pd.read_csv('./data/Matches.csv', low_memory=False)
print(df.shape)

# just EPL
df = df[df['Division'] == "E0"]
print(df.shape)

df = df[df['MatchDate'] > "2023-08-01"]

print(df.columns)
df.drop

print(df.shape)
# prune off lots of columns we wont use - see the ReadMe for the dataset
df = df.drop(columns=['Division', 'HTHome', 'HTAway','HomeTarget','AwayTarget','HomeCorners','AwayCorners', 'HomeYellow', 'AwayYellow','HomeFouls', 'AwayFouls', 'OddHome', 'OddDraw', 'OddAway', 'MaxHome', 'MaxDraw',\
    'MaxAway', 'Over25', 'Under25', 'MaxOver25', 'MaxUnder25', 'HandiSize', 'HandiHome', 'HandiAway'])

# make matchTime just the hour to treat it as a factor
df['MatchTime'] = df['MatchTime'].str.slice(0,2)
df['MatchTime'] = pd.to_numeric(df['MatchTime'], errors='coerce')

# factorize the HTResult and FTresult too, check they are done in same way 

codes, uniques = df['FTResult'].factorize()
df['FTResFactor'] = codes
print(uniques)

# calculate a diff for Elo
df['EloDiff'] = df['HomeElo'] - df['AwayElo']
print(df.head())
print(df.tail())

print(df[['MatchTime', 'FTResFactor', 'HomeRed', 'AwayRed','EloDiff','HomeShots', 'AwayShots' ]].corr())   

