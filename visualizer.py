import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

INPUT_FILE = "Bangladesh_Economy_analyzed_data.csv"
print(f"Starting visualization for: {INPUT_FILE}")

try:
    df = pd.read_csv(INPUT_FILE)
except FileNotFoundError:
    print(f"❌ Error: File not found. Please make sure {INPUT_FILE} is in the same folder.")
    exit()

sentiment_counts = df['Sentiment_Label'].value_counts()
labels = sentiment_counts.index
sizes = sentiment_counts.values

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Overall Sentiment Distribution of News Articles', fontsize=15)
plt.axis('equal')
plt.savefig('sentiment_pie_chart.png')
print("✅ Pie Chart saved as: sentiment_pie_chart.png")

df['publishedAt'] = pd.to_datetime(df['publishedAt'])

trend_df = df[df['Sentiment_Label'] != 'Neutral'].copy()
trend_df['Date'] = trend_df['publishedAt'].dt.date
sentiment_trend = trend_df.groupby(['Date', 'Sentiment_Label']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 6))
sentiment_trend.plot(kind='bar', stacked=True, color={'Positive': 'lightgreen', 'Negative': 'salmon'}, ax=plt.gca())
plt.title('Sentiment Trend Over Time', fontsize=15)
plt.xlabel('Publication Date')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Sentiment')
plt.tight_layout()

plt.savefig('sentiment_trend_bar_chart.png')
print("✅ Trend Chart saved as: sentiment_trend_bar_chart.png")
print("\nVisualization complete. Check your folder for the two image files.")