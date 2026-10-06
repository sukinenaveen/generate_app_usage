import pandas as pd
import numpy as np
df = pd.read_csv("day02_usage.csv")
Chat = df["Chat"].to_numpy()
Video = df["Video"].to_numpy()
Study = df["Study"].to_numpy()
Games = df["Games"].to_numpy()
print(len(Chat))
print("Total Usage")
print(Chat.sum())
print(Video.sum())
print(Study.sum())
print(Games.sum())
print("Average Usage")
print(round(Chat.mean(), 1))
print(round(Video.mean(), 1))
print(round(Study.mean(), 1))
print(round(Games.mean(), 1))
print("Max Usage")
print(max([Chat.max(), Video.max(), Study.max(), Games.max()]))
new_array=Study-Games
print("Best Day for Study vs Games")
print(new_array.argmax()+1)
print("Worst Day for Study vs Games")
print(new_array.argmin()+1)
apps=["Chat", "Video", "Study", "Games"]
for i in range(30):
    values=[Chat[i], Video[i], Study[i], Games[i]]
    print("Day", i+1, ":", apps[np.argmax(values)], "is the most used app with", max(values), "minutes of usage.")

daily_total = Chat + Video + Study + Games

Chat_share = Chat / daily_total * 100
Video_share = Video / daily_total * 100
Study_share = Study / daily_total * 100
Games_share = Games / daily_total * 100
print(Chat_share)
print(Video_share)
print(Study_share)
print(Games_share)