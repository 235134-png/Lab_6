import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
raw_data = {
    "Date": [
        "2026-03-01", "2026-03-02", "2026-03-03", "2026-03-04",
        "2026-03-05", "2026-03-06", "2026-03-07", "2026-03-08",
        "2026-03-09", "2026-03-10", "2026-03-11", "2026-03-12",
        "2026-03-13", "2026-03-14", "2026-03-15", "2026-03-03"
    ],
    "City": [
        "Islamabad", " islamabad", "ISLAMABAD ", "Islamabad",
        " Islamabad", "ISLAMABAD", "Islamabad", "islamabad",
        "Islamabad", "ISLAMABAD ", "Islamabad", " islamabad",
        "Islamabad", "Islamabad", "ISLAMABAD", "ISLAMABAD "
    ],
    "Temperature": [
        "22C", "24C", "20C", "18C",
        "25C", "28C", "27C", "23C",
        "21C", "19C", "26C", "29C",
        "30C", "22C", "24C", "20C"
    ],
    "Humidity": [
        55.0, 50.0, np.nan, 75.0,
        45.0, 40.0, np.nan, 60.0,
        65.0, 70.0, np.nan, 38.0,
        35.0, 58.0, 52.0, np.nan
    ],
    "Condition": [
        "sunny", "Sunny", " Rainy", "CLOUDY ",
        "sunny", "Sunny ", " cloudy", "Rainy",
        "cloudy", "Rainy", "sunny", "Sunny",
        "sunny", "cloudy", "cloudy", " Rainy"
    ]
}

df = pd.DataFrame(raw_data)
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()
df["Temperature"] = df["Temperature"].str.replace("C", "", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])

df = df.drop_duplicates()
print(f"Rows after dropping duplicates: {len(df)}")

median_hum = df["Humidity"].median()
df["Humidity"] = df["Humidity"].fillna(median_hum)
print(f"Missing Humidity filled with median: {median_hum}")

corr = df["Temperature"].corr(df["Humidity"])
print(f"Correlation (Temperature, Humidity): {corr:.2f}")
encoded_df = pd.get_dummies(df, columns=["Condition"], dtype=int)
condition_cols = [c for c in encoded_df.columns if c.startswith("Condition_")]
print("\nOne-hot Encoded Condition Columns:")
print(encoded_df[condition_cols].head())

cond_counts = df["Condition"].value_counts()
print("\nCondition counts:")
print(cond_counts)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(df["Date"].dt.strftime("%m-%d"), df["Temperature"], marker="o", color="tab:red")
axes[0, 0].set_title("Temperature Trend (°C)")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (°C)")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(True, linestyle="--", alpha=0.5)

axes[0, 1].scatter(df["Temperature"], df["Humidity"], color="tab:blue", s=50)
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (°C)")
axes[0, 1].set_ylabel("Humidity (%)")
axes[0, 1].grid(True, linestyle="--", alpha=0.5)

axes[1, 0].pie(cond_counts.values, labels=cond_counts.index, autopct="%1.1f%%", startangle=140, colors=["#FF9999", "#66B2FF", "#99FF99"])
axes[1, 0].set_title("Weather Condition Frequency")

axes[1, 1].hist(df["Temperature"], bins=5, color="tab:green", edgecolor="black", alpha=0.7)
axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (°C)")
axes[1, 1].set_ylabel("Frequency")

fig.suptitle("Weather Overview", fontsize=16, fontweight="bold")
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()
print("Saved weather_dashboard.png")
