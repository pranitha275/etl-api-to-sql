import requests
import json

def fetch_data():
    posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    return posts, users

if __name__ == '__main__':
    posts, users = fetch_data()
    with open('posts.json', 'w') as f:
        json.dump(posts, f)
    with open('users.json', 'w') as f:
        json.dump(users, f)
    print(f"Fetched and saved {len(posts)} posts and {len(users)} users")