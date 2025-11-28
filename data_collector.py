import requests
import pandas as pd
import json

API_KEY = "4a4b704d71524eb696d7dd287e0fac11"
QUERY = "Bangladesh Economy"  
LANGUAGE = "en" 
PAGE_SIZE = 100 
print(f"Starting data collection for: {QUERY}")

url = f"https://newsapi.org/v2/everything?q={QUERY}&language={LANGUAGE}&pageSize={PAGE_SIZE}&apiKey={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()  
    data = response.json()
    articles = data.get('articles', [])
    print(f"Successfully retrieved {len(articles)} articles.")
    
    if articles:
        df = pd.DataFrame(articles)
        cols_to_keep = ['title', 'description', 'content', 'url', 'publishedAt']
        df = df[cols_to_keep]
        output_filename = f"{QUERY.replace(' ', '_')}_news_data.csv"
        df.to_csv(output_filename, index=False, encoding='utf-8')
        
        print(f"\n✅ Success! Data saved to: {output_filename}")
        print("\nFirst 5 rows of data:")
        print(df.head())
    else:
        print("⚠ Warning: No articles found for this query. Check your API Key or change the query.")

except requests.exceptions.HTTPError as err:
    print(f"\n❌ Error: HTTP Error occurred. Check your API Key or Quota.")
    print(f"Details: {err}")
except Exception as e:
    print(f"\n❌ An unexpected error occurred: {e}")