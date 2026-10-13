
import pandas as pd
import numpy as np

df = pd.read_csv("day02_usage.csv")
apps = ["Chat", "Video", "Study", "Games"]
table = df[apps].to_numpy()

print("Shape:", table.shape)
print("App totals:", table.sum(axis=0))
print("App averages:", table.mean(axis=0))
print("App maximums:", table.max(axis=0))
print("App minimums:", table.min(axis=0))
print("Day totals:", table.sum(axis=1))
print("Day averages:", table.mean(axis=1))
print("Day maximums:", table.max(axis=1))
print("Day minimums:", table.min(axis=1))

winners = np.array(apps)[table.argmax(axis=1)]
print("Daily winners:", winners)

names, counts = np.unique(winners, return_counts=True)
print("Win counts:")
for name, count in zip(names, counts):
    print(name, count)

day_totals = table.sum(axis=1)
percentages = np.divide(
    table,
    day_totals[:, np.newaxis],
    out=np.zeros_like(table, dtype=float),
    where=day_totals[:, np.newaxis] != 0
) * 100

print("First day percentages:", percentages[0])
print("Percentage total:", percentages[0].sum())

app_maximums = table.max(axis=0)
scaled = np.divide(
    table,
    app_maximums,
    out=np.zeros_like(table, dtype=float),
    where=app_maximums != 0
)

print("Scaled table:", scaled)

days = df["Day"].to_numpy()
weekend_mask = days % 7 >= 6
weekday_mask = ~weekend_mask

print("Weekend averages:", table[weekend_mask].mean(axis=0))
print("Weekday averages:", table[weekday_mask].mean(axis=0))

busiest_index = day_totals.argmax()
print("Busiest day:", days[busiest_index])
print("Total minutes:", day_totals[busiest_index])
