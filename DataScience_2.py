import pandas as pd

df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]});

print(df);

df.ix[df.AAA >= 5, 'BBB'] = -1
# print(df)
# print("-----------------")
# print(df["AAA"])
print(df[0:2])