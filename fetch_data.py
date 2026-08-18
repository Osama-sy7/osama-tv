import os, json, requests
API_KEY = os.environ.get("TMDB_API_KEY")
url = f"https://api.themoviedb.org/3/trending/all/week?api_key={API_KEY}&language=ar"
data = {"movies": requests.get(url).json().get('results', [])}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
