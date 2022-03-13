import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('Assets\CONVICTIONSUMMARY_270_opt3_best2(1).csv', sep='|')

df2 = pd.DataFrame()
df2 = df.loc[df['TYPE'] == 'MERGED']

print(df2)