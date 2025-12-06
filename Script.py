import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_track = pd.read_csv("input/spotify-datasets/tracks.csv")
print(df_track.head())

# null values
print(df_track.isnull().sum())
print(df_track.shape)
print(df_track.head())

# Sort by popularity
sort_df = df_track.sort_values("popularity", ascending=True)
print(sort_df.head())

# Statistical summary
print(df_track.describe().transpose())
most_popular = df_track[df_track["popularity"] > 90].sort_values(by="popularity", ascending=False)
print(most_popular.head())
print(df_track[["artists"]].iloc[18])

# Convert duration from ms to seconds
df_track["duration"] = df_track["duration_ms"].apply(lambda x: round(x / 1000))
df_track.drop("duration_ms", inplace=True, axis=1)
print(df_track.head())

# Artists with most songs
print(df_track["artists"].value_counts())

# Dataframe info
print(df_track.info())

# Find artist with specific song duration
print(df_track[df_track["duration"] == 5621]["artists"])

# Correlation heatmap
corr_df = df_track.select_dtypes(include=[np.number]).drop(["key", "mode", "explicit"], axis=1).corr(method="pearson")
heatmap = sns.heatmap(corr_df, annot=True, vmin=-1, vmax=1, center=0, cmap="inferno")
heatmap.set_title("Correlation Heatmap")
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)
plt.show()

# Random sample
sample_df = df_track.sample(int(0.004 * len(df_track)))
print(sample_df.head())
print(len(sample_df))

plt.figure(figsize=(10, 8))
sns.regplot(data=sample_df, y="loudness", x="energy", color="c")
plt.title("Loudness vs Energy")
plt.show()

# Popularity vs Acousticness
plt.figure(figsize=(10, 8))
sns.regplot(data=sample_df, y="popularity", x="acousticness", color="c")
plt.title("Popularity vs Acousticness")
plt.show()

df_track["dates"] = pd.to_datetime(df_track["release_date"])
print(df_track.info())

df_track["release_date"] = pd.to_datetime(df_track["release_date"])
df_track["year"] = df_track["release_date"].dt.year
print(df_track.info())

sns.displot(df_track["year"], discrete=True, aspect=2, height=5, kind="hist")
plt.title("Number of Songs per Year")
plt.show()

total_dr = df_track["duration"]
plt.figure(figsize=(12, 6))
sns.barplot(x=df_track["year"], y=total_dr, errwidth=0)
plt.title("Year vs Duration")
plt.xticks(rotation=60)
plt.show()


sns.set_style("whitegrid")
plt.figure(figsize=(12, 5))
sns.lineplot(x=df_track["year"], y=total_dr)
plt.title("Year vs Duration")
plt.xticks(rotation=60)
plt.show()

SpotifyFeatures.csv
df = pd.read_csv("../input/ultimate-spotify-tracks-db/SpotifyFeatures.csv")
print(df.head())

# Duration by genre
plt.title("Duration of Songs Across Genres")
sns.barplot(y=df["genre"], x=df["duration_ms"])
plt.xlabel("Duration (ms)")
plt.ylabel("Genres")
plt.show()

# Top 10 genres by popularity
sns.set_style("darkgrid")
plt.figure(figsize=(10, 5))
famous = df.sort_values("popularity", ascending=False).head(10)
sns.barplot(y="genre", x="popularity", data=famous)
plt.title("Top 10 Genres by Popularity")
plt.show()
