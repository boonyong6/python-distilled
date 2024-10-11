from urllib.request import urlopen

# Example 1: 
#   To fetch a webpage.
u = urlopen("http://www.python.org")
data = u.read()
print(data)


# Example 2:
#   Encode form parameters (dict) into a querystring.
from urllib.parse import urlencode

form = {
    "name": "Mary A. Python",
    "email": "mary123@python.org"
}

data = urlencode(form)  # <--
u = urlopen("http://httpbin.org/post", data.encode("utf-8"))
response = u.read()
print(response)


# Example 3:
#   Parse a URL into 6 components.
from urllib.parse import urlparse

url = "http://httpbin.org/get?name=Dave&n=42"
parse_result = urlparse(url)
print(parse_result)
