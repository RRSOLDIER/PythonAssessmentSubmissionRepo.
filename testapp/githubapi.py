import requests

def search_repositories(query):
    url = f"https://api.github.com/search/repositories?q={query}&per_page=10"
    response = requests.get(url)
    return response.json()