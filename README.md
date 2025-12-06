# 🎵 Spotify Music Data Analysis

<div align="center">

![Project Banner](path/to/your/banner-image.png)

*Uncovering the Patterns Behind 586,672 Songs*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-orange.svg)](https://seaborn.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Overview](#overview) • [Features](#features) • [Installation](#installation) • [Results](#results) • [Visualizations](#visualizations)

</div>

---

## 📋 Overview

This project performs comprehensive exploratory data analysis (EDA) on Spotify's music dataset to uncover relationships between audio features, popularity trends, and temporal patterns in music. Using statistical analysis and data visualization, we investigate what makes music popular and how the music industry has evolved over time.

### 🎯 Key Objectives

- Analyze audio feature correlations using Pearson coefficient
- Investigate the relationship between popularity and audio characteristics
- Explore temporal trends in music duration and release patterns
- Compare genre-specific patterns in duration and popularity
- Identify factors that contribute to song success

---

## 🔧 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.8+** | Primary programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **Matplotlib** | Static visualizations |
| **Seaborn** | Statistical data visualization |
| **Jupyter Notebook** | Interactive development environment |

---

## 📊 Dataset Information

### Primary Dataset: `tracks.csv`
- **Total Tracks**: 586,672 songs
- **Features**: 20 columns
- **Source**: Spotify API
- **Time Period**: 1920s - 2020s

### Feature Descriptions

| Feature | Type | Range | Description |
|---------|------|-------|-------------|
| `id` | String | - | Unique Spotify track identifier |
| `name` | String | - | Song title |
| `popularity` | Integer | 0-100 | Popularity score based on streams |
| `duration_ms` | Integer | - | Track length in milliseconds |
| `explicit` | Binary | 0-1 | Contains explicit content |
| `artists` | String | - | Artist name(s) |
| `release_date` | Date | - | Release date |
| `danceability` | Float | 0-1 | How suitable for dancing |
| `energy` | Float | 0-1 | Intensity and activity measure |
| `key` | Integer | 0-11 | Musical key (C, C#, D, etc.) |
| `loudness` | Float | -60-0 | Overall loudness in decibels |
| `mode` | Binary | 0-1 | Major (1) or Minor (0) |
| `speechiness` | Float | 0-1 | Presence of spoken words |
| `acousticness` | Float | 0-1 | Confidence of acoustic sound |
| `instrumentalness` | Float | 0-1 | Predicts lack of vocals |
| `liveness` | Float | 0-1 | Presence of audience |
| `valence` | Float | 0-1 | Musical positiveness/happiness |
| `tempo` | Float | 0-250+ | Beats per minute (BPM) |
| `time_signature` | Integer | 3-7 | Time signature (beats per bar) |

---

## 🚀 Installation

### Prerequisites
```bash
Python 3.8 or higher
pip package manager
```

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/spotify-music-analysis.git
cd spotify-music-analysis
```

2. **Create virtual environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download dataset**
- Place `tracks.csv` in `input/spotify-datasets/`
- Place `SpotifyFeatures.csv` in `input/ultimate-spotify-tracks-db/`

5. **Run the analysis**
```bash
python Script.py
```

---

## 📈 Key Findings

### 1. Correlation Analysis

Our correlation heatmap revealed several significant relationships:

#### 🔥 Strong Positive Correlations
| Feature Pair | Correlation | Interpretation |
|--------------|-------------|----------------|
| **Energy ↔ Loudness** | **0.76** | High-energy songs are significantly louder |
| **Danceability ↔ Valence** | **0.53** | Danceable songs tend to be happier/more positive |
| **Energy ↔ Valence** | **0.37** | Energetic songs are more likely to be upbeat |

#### 🧊 Strong Negative Correlations
| Feature Pair | Correlation | Interpretation |
|--------------|-------------|----------------|
| **Energy ↔ Acousticness** | **-0.72** | Acoustic songs are typically less energetic |
| **Loudness ↔ Acousticness** | **-0.52** | Acoustic tracks are quieter than produced tracks |
| **Popularity ↔ Acousticness** | **-0.37** | Popular songs tend to be more produced/electronic |

### 2. The Popularity Paradox

> **Critical Finding**: Audio features alone cannot predict song popularity!

| Feature vs Popularity | Correlation | Conclusion |
|----------------------|-------------|------------|
| Danceability | 0.19 | Weak |
| Energy | 0.30 | Weak |
| Loudness | 0.33 | Weak |
| Valence | 0.0046 | Negligible |
| Acousticness | -0.37 | Moderate (strongest) |

**Implication**: Song success depends on non-audio factors:
- Artist reputation and fanbase
- Marketing and promotion
- Cultural timing and trends
- Playlist placement
- Social media virality
- Music video quality

### 3. Temporal Trends

#### Song Duration Over Time
- **1960s-1980s**: Average ~210 seconds (3.5 minutes)
- **1990s-2000s**: Peak at ~240 seconds (4 minutes)
- **2010s-2020s**: Decline to ~200 seconds (3.3 minutes)

**Explanation**: 
- Streaming era economics (payment per stream)
- Shorter attention spans
- Playlist culture (skip rates)
- TikTok and social media influence

#### Release Volume Trends
- **Pre-2000**: Limited digital presence (~5K songs/year)
- **2000-2010**: Digital transition (~20K songs/year)
- **2010-2020**: Streaming boom (~50K+ songs/year)

### 4. Statistical Summary

| Metric | Mean | Median | Std Dev |
|--------|------|--------|---------|
| **Popularity** | 27.57 | 24.00 | 21.82 |
| **Duration (s)** | 230.05 | 223.53 | 98.70 |
| **Danceability** | 0.564 | 0.581 | 0.177 |
| **Energy** | 0.542 | 0.564 | 0.264 |
| **Valence** | 0.552 | 0.569 | 0.248 |
| **Tempo (BPM)** | 118.46 | 119.95 | 30.04 |

**Key Insights**:
- Most songs have low popularity (mean = 27.57/100)
- Songs are moderately danceable and energetic
- Wide variation in energy and valence (high std dev)

### 5. Top Artists by Track Count

| Rank | Artist | Track Count | Genre/Type |
|------|--------|-------------|------------|
| 1 | Die drei ??? | 3,856 | German audio drama |
| 2 | TKKG Retro-Archiv | 2,006 | German audio drama |
| 3 | Benjamin Blümchen | 1,503 | Children's audiobook |
| 4 | Bibi Blocksberg | 1,472 | Children's audiobook |
| 5 | Lata Mangeshkar | 1,373 | Bollywood playback singer |

**Note**: High track counts indicate audiobook series and prolific recording artists.

---

## 📊 Visualizations

### 1. Correlation Heatmap
![Correlation Heatmap](output/correlation_heatmap.png)

**Description**: Comprehensive view of relationships between all numeric audio features. Color intensity indicates correlation strength (yellow = positive, purple = negative).

**Key Observations**:
- Diagonal shows perfect correlation (1.0) of each feature with itself
- Energy-Loudness shows strongest positive relationship
- Energy-Acousticness shows strongest negative relationship

---

### 2. Loudness vs Energy Regression
![Loudness vs Energy](output/loudness_vs_energy.png)

**Description**: Strong positive relationship (r=0.76) demonstrating that high-energy tracks are consistently louder. The tight clustering around the regression line indicates a reliable pattern.

**Interpretation**: 
- Upward slope confirms positive correlation
- Low scatter indicates strong predictive power
- Energy can be used as a proxy for loudness in many cases

---

### 3. Popularity vs Acousticness Regression
![Popularity vs Acousticness](output/popularity_vs_acousticness.png)

**Description**: Moderate negative relationship (r=-0.37) showing popular songs tend to be less acoustic. Wide scatter indicates other factors strongly influence popularity.

**Interpretation**:
- Downward slope shows negative correlation
- High scatter indicates low predictive power
- Acoustic songs can still achieve popularity through other means

---

### 4. Song Releases Over Time
![Release Distribution](output/songs_per_year.png)

**Description**: Exponential growth in digitally available music, particularly after 2000, reflecting the streaming revolution.

**Key Trends**:
- Dramatic increase post-2000 (digital age)
- Accelerated growth post-2010 (streaming era)
- Peak in recent years due to easier music distribution

---

### 5. Duration Trends by Year (Bar Plot)
![Duration Trends Bar](output/duration_vs_year_bar.png)

**Description**: Bar chart showing average song duration trends across decades, revealing the shift toward shorter tracks in the streaming era.

**Findings**:
- Peak duration in 1990s-2000s
- Clear downward trend in 2010s-2020s
- Modern songs average 30-60 seconds shorter

---

### 6. Duration Trends by Year (Line Plot)
![Duration Trends Line](output/duration_vs_year_line.png)

**Description**: Line plot with confidence intervals showing the same duration trend, highlighting the consistency of the shortening pattern.

**Statistical Insight**:
- Smooth trend line confirms systematic change
- Narrow confidence intervals show high certainty
- Pattern is not random fluctuation

---

### 7. Duration by Genre
![Genre Duration](output/duration_by_genre.png)

**Description**: Horizontal bar chart comparing average song duration across different genres.

**Genre Patterns**:
- **Longest**: Classical, Opera, Jazz (5-8 minutes)
- **Medium**: Rock, R&B, Blues (3-5 minutes)
- **Shortest**: Pop, EDM, Hip-Hop (2.5-3.5 minutes)

---

### 8. Top Genres by Popularity
![Top Genres](output/top_genres_popularity.png)

**Description**: Shows which genres dominate among the most popular tracks in the dataset.

**Insights**:
- Mainstream genres (Pop, Hip-Hop) lead popularity charts
- Electronic/Dance music shows strong presence
- Genre diversity in top tracks is limited

---

## 💡 Business Insights

### For Record Labels
✅ **Production Focus**: Invest in high-energy, well-produced tracks over purely acoustic ones  
✅ **Marketing Matters**: Audio quality alone doesn't guarantee success; marketing budget is crucial  
✅ **Duration Strategy**: Consider 3-minute format for maximum streaming potential  
✅ **Genre Selection**: Pop and Hip-Hop show highest popularity potential

### For Artists
✅ **Genre Alignment**: Understand your genre's typical audio profile  
✅ **Acoustic Balance**: Pure acoustic may limit mainstream appeal  
✅ **Energy Optimization**: Higher energy correlates with better engagement  
✅ **Strategic Length**: Keep tracks concise for playlist inclusion

### For Streaming Platforms
✅ **Recommendation Algorithms**: Use multi-feature similarity (not single-feature matching)  
✅ **Playlist Curation**: Balance energy and valence for mood-based playlists  
✅ **Discovery Features**: Don't over-rely on audio features; incorporate social signals  
✅ **Trend Adaptation**: Account for evolving duration preferences

---

## 🔬 Methodology

### Data Cleaning
1. Handled 71 missing values in `name` column
2. Converted duration from milliseconds to seconds
3. Parsed release dates to datetime format
4. Extracted year component for temporal analysis
5. Removed non-numeric columns for correlation analysis

### Statistical Approach
- **Correlation Method**: Pearson coefficient
- **Sampling Strategy**: 0.4% random sample for visualization (n=2,347)
- **Significance Level**: α = 0.05
- **Confidence Intervals**: 95% for regression plots
- **Visualization Library**: Seaborn with Matplotlib backend

### Analysis Pipeline
```
Data Loading → Quality Check → Transformation → 
Statistical Analysis → Correlation Computation → 
Visualization → Temporal Analysis → Genre Comparison
```

### Code Workflow
```python
# 1. Load and explore data
df_track = pd.read_csv("tracks.csv")

# 2. Clean and transform
df_track["duration"] = df_track["duration_ms"] / 1000
df_track["year"] = pd.to_datetime(df_track["release_date"]).dt.year

# 3. Correlation analysis
corr_df = df_track.select_dtypes(include=[np.number]).drop(
    ["key", "mode", "explicit"], axis=1
).corr(method="pearson")

# 4. Visualize patterns
sns.heatmap(corr_df, annot=True, cmap="inferno")

# 5. Temporal analysis
sns.lineplot(x="year", y="duration", data=df_track)
```

---

## 📁 Project Structure

```
spotify-music-analysis/
│
├── input/
│   ├── spotify-datasets/
│   │   └── tracks.csv                    # Main dataset (586K songs)
│   └── ultimate-spotify-tracks-db/
│       └── SpotifyFeatures.csv          # Genre dataset
│
├── output/
│   ├── correlation_heatmap.png          # Feature correlation matrix
│   ├── loudness_vs_energy.png           # Regression plot
│   ├── popularity_vs_acousticness.png   # Regression plot
│   ├── songs_per_year.png               # Distribution histogram
│   ├── duration_vs_year_bar.png         # Bar chart
│   ├── duration_vs_year_line.png        # Line plot
│   ├── duration_by_genre.png            # Genre comparison
│   └── top_genres_popularity.png        # Top genres chart
│
├── Script.py                            # Main analysis script
├── requirements.txt                     # Python dependencies
├── README.md                           # Project documentation
├── LICENSE                             # MIT License
└── .gitignore                          # Git ignore file
```

---

## 🛠️ Requirements

Create a `requirements.txt` file with:

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scipy>=1.7.0
```

**Installation Command**:
```bash
pip install -r requirements.txt
```

---

## 🎓 Key Learnings

### Statistical Concepts Applied
- **Pearson Correlation**: Measures linear relationships between variables
- **Regression Analysis**: Predicts one variable from another
- **Descriptive Statistics**: Summarizes data distributions
- **Time Series Analysis**: Examines trends over time
- **Sampling Theory**: Represents large datasets efficiently

### Data Science Skills Demonstrated
✅ Data cleaning and preprocessing  
✅ Exploratory data analysis (EDA)  
✅ Statistical correlation analysis  
✅ Data visualization best practices  
✅ Temporal trend identification  
✅ Business insight extraction  

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Ideas
- Add machine learning models for prediction
- Implement interactive dashboards
- Analyze additional datasets
- Create genre classification algorithms
- Build recommendation systems

---

## 📝 Future Enhancements

- [ ] Machine learning model for popularity prediction
- [ ] Sentiment analysis on song lyrics
- [ ] Artist collaboration network analysis
- [ ] Genre classification using audio features
- [ ] Interactive dashboard with Plotly/Dash
- [ ] Recommendation system implementation
- [ ] Real-time Spotify API integration
- [ ] Mood-based playlist generator
- [ ] Audio feature anomaly detection
- [ ] Cross-platform comparison (Spotify vs Apple Music)

---

## 📚 References

- [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api/)
- [Audio Features Explanation](https://developer.spotify.com/documentation/web-api/reference/get-audio-features)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Pearson Correlation Coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)

---

## ❓ FAQ

**Q: Where can I get the dataset?**  
A: The dataset is available on Kaggle. Search for "Spotify Tracks Dataset" or use the API.

**Q: How long does the analysis take to run?**  
A: Approximately 2-5 minutes depending on your system specifications.

**Q: Can I use this for my own project?**  
A: Yes! This project is open-source under MIT License. Attribution is appreciated.

**Q: Why are some correlations negative?**  
A: Negative correlation means as one feature increases, the other decreases (inverse relationship).

**Q: How accurate is the popularity prediction?**  
A: Audio features alone show weak prediction power (r<0.35), confirming that non-audio factors dominate success.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com
- Portfolio: [yourwebsite.com](https://yourwebsite.com)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Acknowledgments

- **Spotify** for providing comprehensive audio feature data through their API
- **Kaggle Community** for curating and sharing the dataset
- **Open Source Contributors** for pandas, matplotlib, seaborn, and numpy
- **Data Science Community** for methodological guidance and best practices

---

## 📊 Project Statistics

![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/spotify-music-analysis)
![GitHub stars](https://img.shields.io/github/stars/yourusername/spotify-music-analysis?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/spotify-music-analysis?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/spotify-music-analysis)

---

## 🌟 Star History

If you found this project helpful, please consider giving it a star! It helps others discover the project.

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/spotify-music-analysis&type=Date)](https://star-history.com/#yourusername/spotify-music-analysis&Date)

---

<div align="center">

### ⭐ If you found this project useful, please give it a star!

**Made with ❤️ and 🎵 by [Your Name]**

---

*"Data is the new music notation." - Anonymous*

</div>