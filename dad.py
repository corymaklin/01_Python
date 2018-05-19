from random import randint
import requests
url = 'https://icanhazdadjoke.com/search'

term = input('Let me tell you a joke! Give me a topic: ')

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": term}
)

data = response.json()
res = data['results']

if len(res) == 0:
    print(f"Sorry I don't have any jokes about {term}! Please try again.")
elif len(res) == 0:
    print(f"I've got one joke about {term}. Here it is:")
    print(res[0]['joke'])
else:
    rand_num = randint(0, len(res)-1)
    print(f"I've got {len(res)} jokes about {term}. Here's one:")
    print(res[rand_num]['joke'])
