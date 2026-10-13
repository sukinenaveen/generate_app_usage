

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("day02_usage.csv")
# arr=df.iloc[:,1:].to_numpy()      --->another way to create 2d
apps=np.array(df.columns)
arr=df[apps].to_numpy()

print(np.shape(arr))

print(f'Mean of the each app {arr.mean(axis=0)}')
print(f'Mean of the usage per each day {arr.mean(axis=1)}')
print(f'Max usage of the each app {arr.max(axis=0)}')
print(f'Max  usage of each day {arr.max(axis=1)}')
print(f'Min of the each app {arr.min(axis=0)}')
print(f'Min usage of each day {arr.min(axis=1)}')

print(f"The Winners of Every Day:{apps[arr.argmax(axis=1)]}")
winners=apps[arr.argmax(axis=1)]
val,freq = np.unique(winners,return_counts=True)
print(dict(zip(val,freq)))

per_day=arr.sum(axis=1)
shares=arr/per_day[:,None]*100

print(f"every app against its peek:{arr/arr.max(axis=0)}")

app_max = arr.max(axis=0)
total = arr / app_max
print(total)
weekend_mask = (df["Day"] % 7 == 6) | (df["Day"] % 7 == 0)
print(df[weekend_mask].mean(axis=0))  
print(df[~weekend_mask].mean(axis=0))

print(per_day.argmax()+1)
#Plot all four apps against the day number with no other instructions. Look at it.
plt.figure(figsize=(10, 6))