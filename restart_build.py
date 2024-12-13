import requests

# Travis CI API details
TRAVIS_API_URL = "https://api.travis-ci.com/repo/<DARKBEASTOP>%2F<Lerelundke>/requests"
TOKEN = "gMIJjlYHTEx7jywvm9-g2Q"

# Headers for Travis CI API
headers = {
    "Travis-API-Version": "3",
    "Authorization": f"token {TOKEN}",
}

# Data to trigger the build
data = {
    "request": {
        "branch": "main"  # Replace with your branch name
    }
}

response = requests.post(TRAVIS_API_URL, json=data, headers=headers)

if response.status_code == 200:
    print("Build triggered successfully!")
else:
    print(f"Failed to trigger build: {response.text}")