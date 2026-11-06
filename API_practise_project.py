import requests
URL = 'https://api.restcountries.com/countries/v5?q=india'

def fetch_post() -> dict:
    # GET request, raise a clear error if the request fails
    response = requests.get(URL, headers={"Authorization": "Bearer rc_live_80c61576a6014de5acc42a0c25c4f400"}, timeout=10)
    print("Status code:", response.status_code)  # the verdict
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()       # Return the parsed JSON data

result = fetch_post()  # Accessing the common name of the country
objects = result["data"]["objects"]
for country in objects:
    if country["names"]["common"] == "India":
        print(country["names"]["common"])