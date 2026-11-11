import requests
import string
title = "COUNTRY EXPLORER"
def title_divider():
    print("=" * 60)
title_divider()
print(title.center(60))
title_divider()
search_term = string.capwords(input("\nEnter search keyword: "))
country_name = string.capwords(input("Enter exact country name to find: "))
title_divider()
URL = f'https://api.restcountries.com/countries/v5?q={search_term}'

def fetch_countries() -> dict:
    # GET request, raise a clear error if the request fails
    response = requests.get(URL, headers={"Authorization": "Bearer rc_live_5450d2c617984884819682e784fae451"}, timeout=10)
    print("Status code:", response.status_code, "\n")  # the verdict
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()       # Return the parsed JSON data

result = fetch_countries()  # Accessing the common name of the country
countries = result["data"]["objects"]
found = False
if countries:
    title_divider()
    print("SEARCH RESULTS".center(60))
    title_divider()
    for number, country in enumerate(countries, start=1):
        if number <= 5:
            print(number, country["names"]["common"])
        if country["names"]["common"] == country_name:
            found = True
            print()
            title_divider()
            print("COUNTRY DETAILS".center(60))
            title_divider()

            print(f"{'Country':<12}: {country['names']['common']}")
            print(f"{'Capital':<12}: {country['capitals'][0]['name']}")
            print(f"{'Population':<12}: {country['population']:,}")
            print(f"{'Area':<12}: {country['area']['kilometers']:,} km²")
            print(f"{'Currencies':<12}: {', '.join([curr['name'] for curr in country['currencies']])}")
            if found and number >= 5:
                break  # Exit the loop after finding the country
            title_divider()
    if not found:
        print(f"No data found for {country_name}. Please check the country name and try again.")
        title_divider()
else:
    print(f"No data found for {country_name}. Please check the country name and try again.")
    title_divider()
    found = False  # Set found to False to display the "not found" message below
