"""
Spotify Data Analysis - Part 1: Data Analysis & Statistics
This script performs data Analysis and saves ALL tables in a SINGLE Excel file.
Each table is saved as a separate sheet in the Excel workbook.
"""

import pandas as pd
import numpy as np
import os

# Create output directory
if not os.path.exists('output'):
    os.makedirs('output')
    print("Created 'output' folder")
else:
    print("'output' folder exists")

try:
    df_track = pd.read_csv("input/spotify-datasets/tracks.csv")
    print("Loaded tracks.csv: {len(df_track):,} songs, {len(df_track.columns)} columns")
except Exception as e:
    print("Error loading tracks.csv: {e}")
    exit(1)

try:
    df_genre = pd.read_csv("input/ultimate-spotify-tracks-db/SpotifyFeatures.csv")
    has_genre_data = True
except Exception as e:
    print(f"Could not load SpotifyFeatures.csv: {e}")
    has_genre_data = False

# create Excel writer
excel_file = 'output/spotify_data_analysis_tables.xlsx'
writer = pd.ExcelWriter(excel_file, engine='openpyxl')

# Data preparation
df_track["duration"] = df_track["duration_ms"].apply(lambda x: round(x / 1000))
df_track.drop("duration_ms", inplace=True, axis=1)
df_track["release_date"] = pd.to_datetime(df_track["release_date"], errors='coerce')
df_track["year"] = df_track["release_date"].dt.year
df_track_clean = df_track.dropna(subset=['year'])

# create sheets
print("\n[1/24] Creating: Table Index...")
sheet_descriptions = {
    'Sheet_Number': list(range(1, 25)),
    'Sheet_Name': [
        '00_INDEX',
        '01_First_5_Rows',
        '02_Null_Values',
        '03_Dimensions',
        '04_Least_Popular',
        '05_Most_Popular',
        '06_Descriptive_Stats',
        '07_Popularity_Dist',
        '08_Duration_Stats',
        '09_Transformed_Sample',
        '10_Top_Artists',
        '11_Correlation_Matrix',
        '12_Positive_Corr',
        '13_Negative_Corr',
        '14_Popularity_Corr',
        '15_Songs_By_Decade',
        '16_Duration_By_Decade',
        '17_Recent_Years',
        '18_Explicit_Content',
        '19_Mode_Distribution',
        '20_Key_Distribution',
        '21_Column_Info',
        '22_Genre_Preview',
        '23_Genre_Stats'
    ],
    'Description': [
        'Index and description of all sheets',
        'First 5 rows of the tracks dataset',
        'Count of null values per column',
        'Dataset dimensions and memory usage',
        'Least popular songs (bottom 10)',
        'Most popular songs (popularity > 90)',
        'Descriptive statistics for numeric features',
        'Popularity distribution statistics',
        'Duration statistics (milliseconds and seconds)',
        'Sample data after transformation',
        'Top 50 artists by track count',
        'Full correlation matrix (Pearson)',
        'Top 20 strongest positive correlations',
        'Top 20 strongest negative correlations',
        'Correlations of all features with popularity',
        'Number of songs released by decade',
        'Average song duration by decade',
        'Songs released in recent 10 years',
        'Distribution of explicit vs non-explicit',
        'Distribution of major vs minor mode',
        'Distribution of musical keys (C, C#, D, etc.)',
        'Column names, data types, and null counts',
        'First 10 rows of genre dataset',
        'Genre statistics and distribution'
    ]
}
# Write sheets
index_df = pd.DataFrame(sheet_descriptions)
index_df.to_excel(writer, sheet_name='00_INDEX', index=False)
df_track.head().to_excel(writer, sheet_name='01_First_5_Rows', index=False)
null_counts = pd.DataFrame({
    'Column': df_track.columns,
    'Null_Count': df_track.isnull().sum().values,
    'Null_Percentage': (df_track.isnull().sum().values / len(df_track) * 100).round(2)
})

null_counts.to_excel(writer, sheet_name='02_Null_Values', index=False)
dimensions = pd.DataFrame({
    'Metric': ['Total_Rows', 'Total_Columns', 'Memory_Usage_MB', 'Unique_Artists'],
    'Value': [
        df_track.shape[0],
        df_track.shape[1],
        round(df_track.memory_usage(deep=True).sum() / 1024**2, 2),
        df_track['artists'].nunique()
    ]
})

dimensions.to_excel(writer, sheet_name='03_Dimensions', index=False)
sort_df = df_track.sort_values("popularity", ascending=True)
sort_df[['name', 'artists', 'popularity', 'year']].head(20).to_excel(
    writer, sheet_name='04_Least_Popular', index=False
)

most_popular = df_track[df_track["popularity"] > 90].sort_values(by="popularity", ascending=False)
if len(most_popular) > 0:
    most_popular[['name', 'artists', 'popularity', 'year']].to_excel(
        writer, sheet_name='05_Most_Popular', index=False
    )
else:
    pd.DataFrame({'Note': ['No songs with popularity > 90']}).to_excel(
        writer, sheet_name='05_Most_Popular', index=False
    )
    
stats = df_track.describe().transpose()
stats.to_excel(writer, sheet_name='06_Descriptive_Stats', index=True)
pop_stats = pd.DataFrame({
    'Metric': ['Mean', 'Median', 'Mode', 'Std_Dev', 'Min', 'Max', 'Q1', 'Q3'],
    'Value': [
        df_track['popularity'].mean(),
        df_track['popularity'].median(),
        df_track['popularity'].mode()[0] if len(df_track['popularity'].mode()) > 0 else np.nan,
        df_track['popularity'].std(),
        df_track['popularity'].min(),
        df_track['popularity'].max(),
        df_track['popularity'].quantile(0.25),
        df_track['popularity'].quantile(0.75)
    ]
})

pop_stats.to_excel(writer, sheet_name='07_Popularity_Dist', index=False)
duration_stats = pd.DataFrame({
    'Metric': ['Mean_Seconds', 'Median_Seconds', 'Min_Seconds', 'Max_Seconds', 'Std_Dev_Seconds'],
    'Value': [
        df_track['duration'].mean(),
        df_track['duration'].median(),
        df_track['duration'].min(),
        df_track['duration'].max(),
        df_track['duration'].std()
    ]
})

duration_stats.to_excel(writer, sheet_name='08_Duration_Stats', index=False)
df_track[['name', 'artists', 'duration', 'popularity', 'year']].head(50).to_excel(
    writer, sheet_name='09_Transformed_Sample', index=False
)
artist_counts = df_track["artists"].value_counts().head(100)
artist_df = pd.DataFrame({
    'Rank': range(1, len(artist_counts) + 1),
    'Artist': artist_counts.index,
    'Track_Count': artist_counts.values
})

artist_df.to_excel(writer, sheet_name='10_Top_Artists', index=False)
corr_df = df_track.select_dtypes(include=[np.number]).drop(
    ["key", "mode", "explicit"], axis=1, errors='ignore'
).corr(method="pearson")
corr_df.to_excel(writer, sheet_name='11_Correlation_Matrix', index=True)
corr_pairs = []
for i in range(len(corr_df.columns)):
    for j in range(i+1, len(corr_df.columns)):
        corr_pairs.append({
            'Feature_1': corr_df.columns[i],
            'Feature_2': corr_df.columns[j],
            'Correlation': corr_df.iloc[i, j]
        })
        
corr_pairs_df = pd.DataFrame(corr_pairs)
positive_corrs = corr_pairs_df[corr_pairs_df['Correlation'] > 0].sort_values(
    'Correlation', ascending=False
).head(30)
positive_corrs['Rank'] = range(1, len(positive_corrs) + 1)
positive_corrs[['Rank', 'Feature_1', 'Feature_2', 'Correlation']].to_excel(
    writer, sheet_name='12_Positive_Corr', index=False
)

negative_corrs = corr_pairs_df[corr_pairs_df['Correlation'] < 0].sort_values(
    'Correlation', ascending=True
).head(30)
negative_corrs['Rank'] = range(1, len(negative_corrs) + 1)
negative_corrs[['Rank', 'Feature_1', 'Feature_2', 'Correlation']].to_excel(
    writer, sheet_name='13_Negative_Corr', index=False
)

pop_corr = corr_df['popularity'].sort_values(ascending=False)
pop_corr_df = pd.DataFrame({
    'Feature': pop_corr.index,
    'Correlation_with_Popularity': pop_corr.values
})

pop_corr_df = pop_corr_df[pop_corr_df['Feature'] != 'popularity']
pop_corr_df['Rank'] = range(1, len(pop_corr_df) + 1)
pop_corr_df[['Rank', 'Feature', 'Correlation_with_Popularity']].to_excel(
    writer, sheet_name='14_Popularity_Corr', index=False
)

df_track_clean['decade'] = (df_track_clean['year'] // 10) * 10
decade_counts = df_track_clean['decade'].value_counts().sort_index()
decade_df = pd.DataFrame({
    'Decade': [f"{int(d)}s" for d in decade_counts.index],
    'Number_of_Songs': decade_counts.values
})

decade_df.to_excel(writer, sheet_name='15_Songs_By_Decade', index=False)
duration_by_decade = df_track_clean.groupby('decade')['duration'].mean().sort_index()
duration_decade_df = pd.DataFrame({
    'Decade': [f"{int(d)}s" for d in duration_by_decade.index],
    'Average_Duration_Seconds': duration_by_decade.values.round(2)
})

duration_decade_df.to_excel(writer, sheet_name='16_Duration_By_Decade', index=False)
recent_years = df_track_clean[df_track_clean['year'] >= df_track_clean['year'].max() - 9]
year_counts = recent_years['year'].value_counts().sort_index()
year_df = pd.DataFrame({
    'Year': year_counts.index.astype(int),
    'Number_of_Songs': year_counts.values
})

year_df.to_excel(writer, sheet_name='17_Recent_Years', index=False)
explicit_counts = df_track['explicit'].value_counts()
explicit_df = pd.DataFrame({
    'Content_Type': ['Non-Explicit (0)', 'Explicit (1)'],
    'Count': [explicit_counts.get(0, 0), explicit_counts.get(1, 0)],
    'Percentage': [
        round(explicit_counts.get(0, 0) / len(df_track) * 100, 2),
        round(explicit_counts.get(1, 0) / len(df_track) * 100, 2)
    ]
})

explicit_df.to_excel(writer, sheet_name='18_Explicit_Content', index=False)
mode_counts = df_track['mode'].value_counts()
mode_df = pd.DataFrame({
    'Mode': ['Minor (0)', 'Major (1)'],
    'Count': [mode_counts.get(0, 0), mode_counts.get(1, 0)],
    'Percentage': [
        round(mode_counts.get(0, 0) / len(df_track) * 100, 2),
        round(mode_counts.get(1, 0) / len(df_track) * 100, 2)
    ]
})

mode_df.to_excel(writer, sheet_name='19_Mode_Distribution', index=False)
key_counts = df_track['key'].value_counts().sort_index()
key_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
key_df = pd.DataFrame({
    'Key': [key_names[k] if 0 <= k < 12 else f'Unknown_{k}' for k in key_counts.index],
    'Count': key_counts.values,
    'Percentage': (key_counts.values / len(df_track) * 100).round(2)
})

key_df.to_excel(writer, sheet_name='20_Key_Distribution', index=False)
col_info = pd.DataFrame({
    'Column': df_track.columns,
    'Data_Type': df_track.dtypes.values.astype(str),
    'Non_Null_Count': df_track.count().values,
    'Null_Count': df_track.isnull().sum().values
})

col_info.to_excel(writer, sheet_name='21_Column_Info', index=False)
print("✓ Sheet: 21_Column_Info")

if has_genre_data:
    print("\n[23/24] Creating: Genre Dataset Preview")
    df_genre.head(50).to_excel(writer, sheet_name='22_Genre_Preview', index=False)
    print("✓ Sheet: 22_Genre_Preview")
    
    print("\n[24/24] Creating: Genre Statistics")
    genre_stats = pd.DataFrame({
        'Genre': df_genre['genre'].value_counts().index[:50],
        'Count': df_genre['genre'].value_counts().values[:50],
        'Avg_Popularity': [df_genre[df_genre['genre']==g]['popularity'].mean() for g in df_genre['genre'].value_counts().index[:50]],
        'Avg_Duration_ms': [df_genre[df_genre['genre']==g]['duration_ms'].mean() for g in df_genre['genre'].value_counts().index[:50]]
    })
    genre_stats.to_excel(writer, sheet_name='23_Genre_Stats', index=False)
    print("✓ Sheet: 23_Genre_Stats")
else:
    print("\n[23-24/24] Skipping: Genre sheets (dataset not available)")
    pd.DataFrame({'Note': ['Genre dataset not found']}).to_excel(
        writer, sheet_name='22_Genre_Preview', index=False
    )
    pd.DataFrame({'Note': ['Genre dataset not found']}).to_excel(
        writer, sheet_name='23_Genre_Stats', index=False
    )
writer.close()
file_size = os.path.getsize(excel_file) / 1024
print("SUCCESS!")