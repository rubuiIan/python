import requests
import json

news_url = "http://api.mediastack.com/v1/news"

news_parameters = {
    "access_key": "6234dc85ceeb3a9ea08b3c215c4e449d",
    "categories": "sports",
    "sources": "cnn, -bbc"
}

news_response = requests.get(news_url, news_parameters)
# print(f"NEWS RESPONSE: {news_response.content}")
parsed_data = news_response.json()

print(json.dumps(parsed_data, indent=4))

# Check if 'data' key exists in the response
if 'data' in parsed_data:
    articles = parsed_data['data']
    
    # Iterate through articles and print titles
    for article in articles:
        title = article.get('title', 'Title not available')
        print(title)
        
else:
    print("No data key found innthe response.")