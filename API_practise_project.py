import requests
import string

country_name = string.capwords(input("Enter the name of a Country: "))
URL = f'https://api.restcountries.com/countries/v5?q={country_name}'

def fetch_countries() -> dict:
    # GET request, raise a clear error if the request fails
    response = requests.get(URL, headers={"Authorization": "Bearer rc_live_80c61576a6014de5acc42a0c25c4f400"}, timeout=10)
    print("Status code:", response.status_code)  # the verdict
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()       # Return the parsed JSON data

result = fetch_countries()  # Accessing the common name of the country
countries = result["data"]["objects"]
found = False
if countries:
    for country in countries:
        if country["names"]["common"] == country_name:
            found = True
            print(f"Data found for {country_name}.")
            print(f"Country: {country['names']['common']}")
            print(f"Capital: {country['capitals'][0]['name']}")
            print(f"Population: {country['population']}")
            print(f"Area: {country['area']['kilometers']} km²")
            print(f"Currencies: {', '.join([curr['name'] for curr in country['currencies']])}")
    if not found:
        print(f"No data found for {country_name}. Please check the country name and try again.")
else:
    print(f"No data found for {country_name}. Please check the country name and try again.")
    found = False  # Set found to False to display the "not found" message below
