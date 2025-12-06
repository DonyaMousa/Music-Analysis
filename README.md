# 🎵 Spotify Music Data Analysis 🎵

<div align="center">

![Project Banner](/assets/Github%20Header%20Banner.png)

*Uncovering the Patterns Behind 586,672 Songs*

[![Linkedin](https://img.shields.io/badge/Linkedin-Follow%20Dev-blue?style=flat-square&logo=Linkedin)](https://www.linkedin.com/in/donya-mousa-628226253/)
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

```bash
spotify-dataset
```
[![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets/code)

```bash
SpotifyFeatures
```

[![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)

---

## 🚀 Installation

### Prerequisites
```bash
Python 3.8 or higher
pip package manager
```
1. **Clone the repository**
```bash
git clone https://github.com/DonyaMousa/Music-Analysis
cd Music-Analysis
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download dataset**
- Place `tracks.csv` in `input/spotify-datasets/`
- Place `SpotifyFeatures.csv` in `input/ultimate-spotify-tracks-db/`

5. **Run**
```bash
python data-analysis.py 
python visualizations.py
```

---

## 📈 Output

### [1. spotify_data_analysis_tables.xlsx](https://github.com/DonyaMousa/Music-Analysis/blob/main/spotify_data_analysis_tables.xlsx)

📊 Single Excel File Contains 24 Sheets:
| ![Sheets](/outputTest/Sheets.png) |


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
![Correlation Heatmap](/outputTest/correlation_heatmap.png)

**Description**: Comprehensive view of relationships between all numeric audio features. Color intensity indicates correlation strength (yellow = positive, purple = negative).

**Key Observations**:
- Diagonal shows perfect correlation (1.0) of each feature with itself
- Energy-Loudness shows strongest positive relationship
- Energy-Acousticness shows strongest negative relationship

---

### 2. Loudness vs Energy Regression
![Loudness vs Energy](/outputTest/loudness_vs_energy.png)

**Description**: Strong positive relationship (r=0.76) demonstrating that high-energy tracks are consistently louder. The tight clustering around the regression line indicates a reliable pattern.

**Interpretation**: 
- Upward slope confirms positive correlation
- Low scatter indicates strong predictive power
- Energy can be used as a proxy for loudness in many cases

---

### 3. Popularity vs Acousticness Regression
![Popularity vs Acousticness](/outputTest/popularity_vs_acousticness.png)

**Description**: Moderate negative relationship (r=-0.37) showing popular songs tend to be less acoustic. Wide scatter indicates other factors strongly influence popularity.

**Interpretation**:
- Downward slope shows negative correlation
- High scatter indicates low predictive power
- Acoustic songs can still achieve popularity through other means

---

### 4. Song Releases Over Time
![Release Distribution](/outputTest/songs_per_year.png)

**Description**: Exponential growth in digitally available music, particularly after 2000, reflecting the streaming revolution.

**Key Trends**:
- Dramatic increase post-2000 (digital age)
- Accelerated growth post-2010 (streaming era)
- Peak in recent years due to easier music distribution

---

### 5. Duration Trends by Year (Bar Plot)
![Duration Trends Bar](/outputTest/duration_vs_year_bar.png)

**Description**: Bar chart showing average song duration trends across decades, revealing the shift toward shorter tracks in the streaming era.

**Findings**:
- Peak duration in 1990s-2000s
- Clear downward trend in 2010s-2020s
- Modern songs average 30-60 seconds shorter

---

### 6. Duration Trends by Year (Line Plot)
![Duration Trends Line](/outputTest/duration_vs_year_line.png)

**Description**: Line plot with confidence intervals showing the same duration trend, highlighting the consistency of the shortening pattern.

**Statistical Insight**:
- Smooth trend line confirms systematic change
- Narrow confidence intervals show high certainty
- Pattern is not random fluctuation

---

### 7. Duration by Genre
![Genre Duration](/outputTest/duration_by_genre.png)

**Description**: Horizontal bar chart comparing average song duration across different genres.

**Genre Patterns**:
- **Longest**: Classical, Opera, Jazz (5-8 minutes)
- **Medium**: Rock, R&B, Blues (3-5 minutes)
- **Shortest**: Pop, EDM, Hip-Hop (2.5-3.5 minutes)

---

### 8. Top Genres by Popularity
![Top Genres](/outputTest/top_genres_popularity.png)

**Description**: Shows which genres dominate among the most popular tracks in the dataset.

**Insights**:
- Mainstream genres (Pop, Hip-Hop) lead popularity charts
- Electronic/Dance music shows strong presence
- Genre diversity in top tracks is limited

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
├── outputTest/
│   ├── correlation_heatmap.png          # Feature correlation matrix
│   ├── loudness_vs_energy.png           # Regression plot
│   ├── popularity_vs_acousticness.png   # Regression plot
│   ├── songs_per_year.png               # Distribution histogram
│   ├── duration_vs_year_bar.png         # Bar chart
│   ├── duration_vs_year_line.png        # Line plot
│   ├── spotify_data_analysis_tables.xlsx# Sheets
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

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

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

## 👨‍💻 Author: Donya Mousa

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DonyaMousa)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/donya-mousa-628226253/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:donyamousv@gmail.com)

---

## 📄 License

This is an open-source project


---

## 📊 Project Statistics

[![GitHub repo size](https://img.shields.io/github/repo-size/DonyaMousa/Music-Analysis)](https://github.com/yourusername/spotify-music-analysis)
![GitHub stars](https://img.shields.io/github/stars/DonyaMousa/Music-Analysis?style=social)
[![GitHub forks](https://img.shields.io/github/forks/DonyaMousa/Music-Analysis?style=social)](https://github.com/yourusername/spotify-music-analysis/network/members)
![GitHub issues](https://img.shields.io/github/issues/DonyaMousa/Music-Analysis) 
---

## 🌟 Star History

If you found this project helpful, please consider giving it a star! It helps others discover the project.

[![Star History Chart](https://api.star-history.com/svg?repos=DonyaMousa/Music-Analysis&type=Date)](https://star-history.com/#yourusername/spotify-music-analysis&Date)

---

<div align="center">

### ⭐ If you found this project useful, please give it a star!

**Made with ❤️ and 🎵**

---


</div>