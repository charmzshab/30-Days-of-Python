import requests
import pprint  # pretty print
import pandas as pd

api_key = "fe921368a73d04eb105670d4327d2d70"

api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmZTkyMTM2OGE3M2QwNGViMTA1NjcwZDQzMjdkMmQ3MCIsInN1YiI6IjVmMGZlNzMwZGZmNjZlMDAzNzdhNTIzOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wz8vmbIhRCOJ6VCLDTFOMsQ893UzPKdx_pPnyLLKKK0"

# HTTP request methods
"""
GET -> grab data
POST -> add/update data

PATCH
PUT
DELETE

"""

# what's our endpoint (or a url)?

# what is the HTTP method that we need?


"""
Endpoint
GET
/movie/{movie_id}

https://api.themoviedb.org/3/movie/550?api_key=fe921368a73d04eb105670d4327d2d70

"""
api_version = 3
movie_id = 550
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
# print(endpoint)

# r = requests.get(endpoint)  # ,data={"api_key": api_key} | ,json={"api_key": api_key}
# print(r.status_code)
# print(r.text)

# using api version 4
api_version = 4
movie_id = 500
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}"
headers = {
    "Authorization": f"Bearer {api_key_v4}",
    "Content-Type": "application/json;charset=utf-8",
}
# print(endpoint)

# r = requests.get(
#     endpoint, headers=headers
# )  # ,data={"api_key": api_key} | ,json={"api_key": api_key}
# print(r.status_code)
# print(r.text)

# search movies

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
# print(endpoint)

r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data["results"]
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result["id"]
            # print(result["title"], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))

output = "movies.csv"
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)

df = pd.DataFrame(movie_data)
# print(df)
df.to_csv(output, index=False)

