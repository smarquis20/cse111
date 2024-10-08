import pandas as pd

df = pd.read_csv('members.csv', index_col='LAST_NAME')

x = df.loc['Marquis', ['FIRST_NAME','EMAIL']]
print(x)
