import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sklearn as skl

df = pd.read_csv('Assets\CONVICTIONSUMMARY_270_opt3_best2(1).csv', sep='|')

df2 = pd.DataFrame()
df2 = df.loc[df['TYPE'] == 'MERGED']

print(df2)

X = df
y = df2[""]
#jak konkretną kolumnę
#jak podejrzeć kolumny

X = df
y = target[“MEDV”]

lm = linear_model.LinearRegression()
model = lm.fit(X,y)
predictions = lm.predict(X)
print(predictions)

lm.score(X,y) #R^2
lm.coef_ 
lm.intercept_ 