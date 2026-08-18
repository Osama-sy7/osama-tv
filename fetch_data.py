import json
import requests

API_KEY = "c72257e5675c44f3e8f98033205d925d"
BASE_URL = "https://api.themoviedb.org/3"

def get_data(endpoint):
    url = f"{BASE_URL}/{endpoint}?api_key={API_KEY}&language=ar-SA&page=1"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json().get('results', [])
    return []

# جلب الأقسام المختلفة
trending_movies = get_data("trending/movie/week")
trending_series = get_data("trending/tv/week")
top_rated_movies = get_data("movie/top_rated")
popular_series = get_data("tv/popular")

data = {
    "trending_movies": trending_movies,
    "trending_series": trending_series,
    "top_rated": top_rated_movies,
    "popular_series": popular_series
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Data successfully updated!")
