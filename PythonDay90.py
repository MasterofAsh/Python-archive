# Exercise 10
# Fetch news from NewsAPI about daily stuff

"""
Use the NewsAPI and the requests module to fetch the daily news related to different topics

Go to: https://newsapi.org/
and explore the various options build your application
"""
import requests

def get_news(topic, api_key):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "apiKey": api_key,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["articles"]

    except requests.exceptions.RequestException as e:
        print(f"Couldn't fetch news: {e}")
        return []

def display_news(articles):
    if not articles:
        print("No articles found.")
        return

    for i, article in enumerate(articles, start=1):
        print(f"\n{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Published: {article['publishedAt']}")
        print(f"   URL: {article['url']}")

api_key = "a33e9cdb13384ef98dd79c8491bb1878"
quit_words = ["quit", "leave", "exit"]

while True:
    topic = input("\nEnter a topic you'd like news about (or type 'quit' to stop): ").strip()

    if topic.lower() in quit_words:
        print("Goodbye!")
        break

    if not topic:
        print("Please enter a topic.")
        continue

    articles = get_news(topic, api_key)
    display_news(articles)