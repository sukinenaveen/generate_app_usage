#```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("day02_usage.csv")

apps = ["Chat", "Video", "Study", "Games"]
usage = df[apps].to_numpy()
days = df["Day"].to_numpy()

per_day = usage.sum(axis=1)
peak_day = int(per_day.argmax())

fig, ax = plt.subplots(figsize=(12, 6))

for i, app in enumerate(apps):
    ax.plot(days, usage[:, i], marker="o", label=app)

ax.legend(loc="upper center", ncol=4)
ax.set_title("Daily App Usage")
ax.set_xlabel("Day")
ax.set_ylabel("Usage (Minutes)")

ax.annotate(
    f"Busiest Day: {days[peak_day]}",
    xy=(days[peak_day], usage[peak_day].max()),
    xytext=(days[peak_day] + 2, usage[peak_day].max() + 20),
    arrowprops=dict(arrowstyle="->", color="black")
)

ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("day02_usage.png", dpi=150)
plt.show()
plt.close(fig)
