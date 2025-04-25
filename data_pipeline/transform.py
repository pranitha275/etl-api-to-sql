import pandas as pd
import json

def transform_data():
    posts = pd.read_json('posts.json')
    users = pd.read_json('users.json')
    df = posts.merge(users, left_on='userId', right_on='id')
    df = df[['userId', 'username', 'email', 'id_x', 'title', 'body']]
    df.rename(columns={'id_x': 'postId', 'title': 'postTitle', 'body': 'postBody'}, inplace=True)
    df.to_csv('transformed_data.csv', index=False)
    print("Data transformed and saved to CSV")

if __name__ == '__main__':
    transform_data()