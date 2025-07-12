import sys
import requests
import json

nums = [1, 2, 3, 4, 5, 6]

URL = "https://icanhazdadjoke.com"

response = requests.get(URL, headers={'Accept': 'Application/json'})
data = response.json()


first, last = sys.argv[1:]

nums_two = [num * 2 for num in nums if num]

# print(nums_two)
print(f"Hello, {first} {last}.\nHere's your joke: {data['joke']}")