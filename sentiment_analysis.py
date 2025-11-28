import pandas as pd
from textblob import TextBlob
import re

INPUT_FILE = "Bangladesh_Economy_news_data.csv"
OUTPUT_FILE = "Bangladesh_Economy_analyzed_data.csv"

print(f"Starting sentiment analysis on: {INPUT_FILE}")

try:
    df = pd.read_csv(INPUT_FILE)
except FileNotFoundError:
    print(f"❌ Error: File not found. Please make sure {INPUT_FILE} is in the same folder.")
    exit()

def clean_text(text):
    if pd.isna(text): 
        return ""
    text = str(text) 
    text = re.sub(r'\[.*?\]', '', text) 
    text = re.sub(r'[^\w\s]', '', text) 
    text = text.lower().strip() 
    return text

def get_sentiment_polarity(text):
    return TextBlob(text).sentiment.polarity

def get_sentiment_label(polarity):
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['clean_description'] = df['description'].apply(clean_text)
df['Sentiment_Polarity'] = df['clean_description'].apply(get_sentiment_polarity)
df['Sentiment_Label'] = df['Sentiment_Polarity'].apply(get_sentiment_label)
df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

print("\n✅ Success! Sentiment analysis complete.")
print(f"Analyzed data saved to: {OUTPUT_FILE}")
print("\nSentiment Distribution:")
print(df['Sentiment_Label'].value_counts()) 
print("\nFirst 5 rows of analyzed data (with new columns):")
print(df[['title', 'Sentiment_Polarity', 'Sentiment_Label']].head())