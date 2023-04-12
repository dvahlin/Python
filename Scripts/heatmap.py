#!/usr/bin/python3
#
#
# Heatmap for parsing CSV
import csv
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Index(['moduleMetadata.PIVY_PARSER.Mutex',
#       'moduleMetadata.PIVY_PARSER.Inject into',
#       'moduleMetadata.PIVY_PARSER.Active Setup Value',
#       'moduleMetadata.PIVY_PARSER.Password', 'moduleMetadata.PIVY_PARSER.ID',
#       'Port', 'C2'],
#      dtype='object')
df = pd.read_csv('file.csv', sep="," ,encoding= 'unicode_escape', header=0, usecols=[1,6])

df1 = df[['Port', 'moduleMetadata.PIVY_PARSER.Mutex']]
counts = pd.crosstab(df1['moduleMetadata.PIVY_PARSER.Mutex'], df['Port']).fillna(0)
#sns.heatmap(counts, cmap="GnBu", annot=True)
sns.heatmap(counts, cmap="GnBu")
plt.show()
