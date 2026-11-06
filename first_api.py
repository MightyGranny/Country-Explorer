import requests


"""What each part does:

-> requests.get(URL): Sends a GET request to the specified URL and returns the response.

-> response.status_code: is the server's verdict:200 - Success, 404 - Not Found, 500 - Internal Server Error, etc.

-> response.json(): converts the server's text to a python dictionary you canindex with post["title"].
"""

"""-------------------------------------------------------"""


# URL : str = "https://jsonplaceholder.typicode.com/posts/999"

# def fetch_post() -> dict:
#     """Sending a GET request and return the parsed JSON body"""
#     response = requests.get(URL, timeout=10)    # timeout: never wait forever
#     response.raise_for_status()                 # Raise an exception for HTTP errors
#     return response.json()                      #JSON text -> Python dict

# if __name__ == "__main__":
#     try:
#         post = fetch_post()
#         print("Status: 200 OK")
#         print("Title: ", post["title"])
#     except requests.exceptions.RequestException as err:
#         print("Request Failed: ", err)

"""-------------------------------------------------------"""
'''
r = requests.get("https://jsonplaceholder.typicode.com/posts/99999", timeout=10)

print("Status code:", r.status_code)  # the verdict

print("Body text:", r.text)           # what did the server actually send back?

# - The server sends back the text of the response, which is usually JSON, but it could be anything.

data = r.json()                       # does this crash or succeed?

# - For this URL, it crashes because there is nothing on that post. It gives error 404 - Not Found.

print("Parsed:", data)

print(data["title"])                  # what happens here?

# This gives an error because the data is an empty dictionary, and there is no "title" key.
'''
#^^^^^^^^^^^^      ^^^^^^^^^^     ^^^^^^^^^^^^^^
# To avoid the crash, we can check the status code before trying to parse the JSON or access its keys. As following:

URL:str = "https://jsonplaceholder.typicode.com/posts/99999"

def fetch_post() -> dict:
    # GET request, raise a clear error if the request fails
    response = requests.get(URL, timeout=10)
    print("Status code:", response.status_code)  # the verdict  
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()       # Return the parsed JSON data

if __name__ == "__main__":
    try:
        post = fetch_post()
        print("Title:", post["title"])
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # e.g., 404 Not Found
    except requests.exceptions.RequestException as req_err:
        print(f"Request failed: {req_err}")  # Other request-related errors
    