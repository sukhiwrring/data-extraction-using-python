import requests
import pprint

api_key = "220036d962ddb07883c6b72b9129f74c"

movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&page=1"
#print(endpoint)
r = requests.get(endpoint) 
#print(r.text)


endpoint_path1 = f"/search/movie"
searh_query = "The Matrix"
endpoint1 = f"{api_base_url}{endpoint_path1}?api_key={api_key}&query={searh_query}"
r1 = requests.get(endpoint1)
pprint.pprint(r1.json())
if r1.status_code in range(200, 299):
    data = r1.json()
    results = data['results']
    if len(results) > 0:
        print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            print(result['title'], _id)
            movie_ids.add(_id)
        print(list(movie_ids))