from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# read the CSV file into a pandas DataFrame
folder = Path(__file__).resolve().parent
df = pd.read_csv(folder / "bicycle_data.csv")

# Date:
#   The date and the hour of the day of observation is floating timestamp
#
# Fremont Bridge Sidewalks, south of N 34th St Total:
#   Total bicycle count of both sidewalk is integer 
#
# Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk:
#   Number of bicycles on west sidewalk is integer 
#
# Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk:
#   Number of bicycles on east sidewalk is integer

east_col = "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"
west_col = "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"
total_col = "Fremont Bridge Sidewalks, south of N 34th St Total"

# convert date value to datetime format
df["Date"] = pd.to_datetime(
    df["Date"], format="%m/%d/%Y %I:%M:%S %p"
)

# convert to values to Int64 to address missing values
for col in [east_col, west_col, total_col]:
    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

# Total bicycle count (East + West).
df["Total"] = df[east_col] + df[west_col]

# Hour of the day (0-23).
df["Hour"] = df["Date"].dt.hour

# Year.
df["Year"] = df["Date"].dt.year


# new DataFrame containing only 2016 data
df_2016 = df[df["Year"] == 2016].copy()


# check for missing data in 2016.

# Number of time points with missing data: 1

missing_count = df_2016[[east_col, west_col]].isna().any(axis=1).sum()

print("Number of missing data points:", missing_count)

# drop missing rows
df_2016 = df_2016.dropna(subset=[east_col, west_col])


# plot the average bicycle counts by hour of the day.

# Compute average total bicycle count for each hour.
hourly_counts = df_2016.groupby("Hour")["Total"].mean()

plt.figure(figsize=(10, 6))

hourly_counts.plot(kind="bar")

plt.title("Average Fremont Bridge Bicycle Counts by Hour in 2016")
plt.xlabel("Hour of the Day")
plt.ylabel("Average Total Bicycle Count")

plt.xticks(rotation=0)
plt.tight_layout()

# save the plot
plt.savefig(folder / "counts_by_hour.png")
plt.close()


# the busiest hour of the day.
#
# Busiest hour in 2016: 17 (5:00 PM - 5:59 PM).

busiest_hour = hourly_counts.idxmax()
average_count = hourly_counts.max()

print("Busiest hour of the day:", busiest_hour)
