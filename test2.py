import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:/Users/Snak00s/Desktop/coding/test/pour test2/calcul du temps.csv")

df_value = df[['Duration', 'Pulse', 'Maxpulse', 'Calories']].dropna()

df_value.loc[7, 'Duration'] = 45

corrdf = df_value.corr()

corrdf.to_csv("C:/Users/Snak00s/Desktop/coding/test/pour test2/corr.csv", index=False)