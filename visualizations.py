"""
Spotify Data Analysis - Part 2: Visualizations
This script generates all visualizations and saves them to the output folder.
Run this after 1_data_analysis.py
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Create output directory
if not os.path.exists('output'):
    os.makedirs('output')
    print("Created 'output' folder")
else:
    print("'output' folder exists")

try:
    df_track = pd.read_csv("input/spotify-datasets/tracks.csv")
    print(f"Loaded: {len(df_track):,} songs")
    
    # Data preparation
    df_track["duration"] = df_track["duration_ms"].apply(lambda x: round(x / 1000))
    df_track.drop("duration_ms", inplace=True, axis=1)
    df_track["release_date"] = pd.to_datetime(df_track["release_date"], errors='coerce')
    df_track["year"] = df_track["release_date"].dt.year
    df_track_clean = df_track.dropna(subset=['year'])
except Exception as e:
    print(f"Error: {e}")
    exit(1)
    
# 1
try:
    corr_df = df_track.select_dtypes(include=[np.number]).drop(
        ["key", "mode", "explicit"], axis=1, errors='ignore'
    ).corr(method="pearson")
    
    plt.figure(figsize=(12, 10))
    heatmap = sns.heatmap(
        corr_df, 
        annot=True, 
        vmin=-1, 
        vmax=1, 
        center=0, 
        cmap="inferno", 
        fmt='.2f', 
        linewidths=0.5,
        cbar_kws={'label': 'Correlation Coefficient'}
    )
    heatmap.set_title("Correlation Heatmap - Audio Features", fontsize=16, fontweight='bold', pad=20)
    heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)
    plt.tight_layout()
    plt.savefig('output/1_correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
except Exception as e:
    print(f"Error: {e}")
    
# 2
try:
    sample_df = df_track.sample(min(3000, len(df_track)))
    
    plt.figure(figsize=(10, 8))
    sns.regplot(
        data=sample_df, 
        y="loudness", 
        x="energy", 
        color="c", 
        scatter_kws={'alpha':0.5, 's': 30}
    )
    plt.title("Loudness vs Energy\n(r = 0.76)", fontsize=14, fontweight='bold')
    plt.xlabel("Energy", fontsize=12)
    plt.ylabel("Loudness (dB)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/2_loudness_vs_energy.png', dpi=300, bbox_inches='tight')
    plt.close()
except Exception as e:
    print("Error: {e}")

# 3
try:
    plt.figure(figsize=(10, 8))
    sns.regplot(
        data=sample_df, 
        y="popularity", 
        x="acousticness", 
        color="c", 
        scatter_kws={'alpha':0.5, 's': 30}
    )
    plt.title("Popularity vs Acousticness\n(r = -0.37)", fontsize=14, fontweight='bold')
    plt.xlabel("Acousticness", fontsize=12)
    plt.ylabel("Popularity", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/3_popularity_vs_acousticness.png', dpi=300, bbox_inches='tight')
    plt.close()
except Exception as e:
    print("Error: {e}")

# 4
try:
    plt.figure(figsize=(14, 6))
    year_counts = df_track_clean['year'].value_counts().sort_index()
    plt.bar(year_counts.index, year_counts.values, color='skyblue', edgecolor='black', width=0.8)
    plt.title("Number of Songs Released Per Year", fontsize=14, fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Number of Songs", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig('output/4_songs_per_year.png', dpi=300, bbox_inches='tight')
    plt.close()
except Exception as e:
    print("Error: {e}")

# 5
try:
    plt.figure(figsize=(14, 6))
    duration_by_year = df_track_clean.groupby('year')['duration'].mean()
    plt.bar(duration_by_year.index, duration_by_year.values, color='coral', edgecolor='black', width=0.8)
    plt.title("Average Song Duration by Year", fontsize=14, fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Duration (seconds)", fontsize=12)
    plt.xticks(rotation=60)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig('output/5_duration_vs_year_bar.png', dpi=300, bbox_inches='tight')
    plt.close()
except Exception as e:
    print("Error: {e}")

# 6
try:
    sns.set_style("whitegrid")
    plt.figure(figsize=(14, 6))
    duration_by_year = df_track_clean.groupby('year')['duration'].mean()
    plt.plot(duration_by_year.index, duration_by_year.values, color='darkblue', linewidth=2, marker='o', markersize=3)
    plt.title("Song Duration Trend Over Time", fontsize=14, fontweight='bold')
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Duration (seconds)", fontsize=12)
    plt.xticks(rotation=60)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/6_duration_vs_year_line.png', dpi=300, bbox_inches='tight')
    plt.close()
except Exception as e:
    print("Error: {e}")

# 7 & 8
try:
    df_genre = pd.read_csv("input/ultimate-spotify-tracks-db/SpotifyFeatures.csv")
    print("Loaded genre dataset: {len(df_genre):,} songs")
    try:
        plt.figure(figsize=(12, 8))
        genre_duration = df_genre.groupby('genre')['duration_ms'].mean().sort_values(ascending=True)
        sns.barplot(y=genre_duration.index, x=genre_duration.values, palette='viridis')
        plt.title("Average Song Duration Across Genres", fontsize=14, fontweight='bold')
        plt.xlabel("Duration (ms)", fontsize=12)
        plt.ylabel("Genres", fontsize=12)
        plt.tight_layout()
        plt.savefig('output/7_duration_by_genre.png', dpi=300, bbox_inches='tight')
        plt.close()
    except Exception as e:
        print("Error: {e}")
    
    try:
        plt.figure(figsize=(12, 6))
        top_songs = df_genre.nlargest(100, 'popularity')
        genre_counts = top_songs['genre'].value_counts().head(10)
        sns.barplot(y=genre_counts.index, x=genre_counts.values, palette='rocket')
        plt.title("Top Genres Among Most Popular Songs (Top 100)", fontsize=14, fontweight='bold')
        plt.xlabel("Number of Songs", fontsize=12)
        plt.ylabel("Genre", fontsize=12)
        plt.tight_layout()
        plt.savefig('output/8_top_genres_popularity.png', dpi=300, bbox_inches='tight')
        plt.close()
    except Exception as e:
        print("Error: {e}")
        
except FileNotFoundError:
    print("Genre dataset not found & skipping plots 7 & 8")
except Exception as e:
    print(f"Error: {e}")

created_files = sorted([f for f in os.listdir('output') if f.endswith('.png')])
print("\nCreated {len(created_files)} visualization(s):\n")
if len(created_files) >= 6:
    print("\nSUCCESS! All main visualizations created.")
else:
    print("\nOnly {len(created_files)} files created.")