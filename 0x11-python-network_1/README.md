# 0x11. Python - Network #1

This README provides a comprehensive guide on fetching internet resources, decoding responses, and making HTTP requests in Python using `urllib` and `requests` packages.

## Fetching Internet Resources with urllib

[`urllib`](https://docs.python.org/3/library/urllib.html) is a Python module that provides a set of URL handling modules. To fetch internet resources, you can use the following steps:

```python
import urllib.request

url = "https://example.com"
response = urllib.request.urlopen(url)
content = response.read()

print(content)
```

## Decoding urllib Body Response

To decode the body response from `urllib`, you can use the following:

```python
decoded_content = content.decode("utf-8")
print(decoded_content)
```

## Using the Python Package requests

`requests` is a popular third-party library that simplifies HTTP requests. Install it using:

```bash
pip install requests
```

## Making HTTP GET Request

To make a GET request with `requests`:

```python
import requests

url = "https://example.com"
response = requests.get(url)

print(response.text)
```

## Making HTTP POST/PUT/etc. Request

For other HTTP methods like POST, PUT, etc., you can use:

```python
data = {"key": "value"}
response = requests.post(url, data=data)

print(response.text)
```

## Fetching JSON Resources

To fetch JSON resources and parse them:

```python
response = requests.get("https://api.example.com/data.json")
json_data = response.json()

print(json_data)
```

## Manipulating Data from an External Service

Once you have the data, you can manipulate it based on your requirements. For example:

```python
for item in json_data["items"]:
    print(item["name"])
```

## Author 🖊️:
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17
