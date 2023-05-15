import praw
import datetime

reddit = praw.Reddit(
    client_id = 'SQ1brEErRrI_T7HCQJtYiQ',
    client_secret = 'DZPHSYnbVaNV5eA0Tw7Jei_BMje2Pg',
    redirect_uri='http://localhost:8000',
    user_agent = 'webapp:AI_Ethics_Crawler:v1.0 (by u/CuriousStardstSpirit).',
    user_name = 'CuriousStardstSpirit'
    )

reddit.read_only = True
#Function to gather the intended data
def get_thread_data(thread_url):
    subreddit = reddit.subreddit(thread_url)
    print(subreddit.title)
    data = {
        'title' : subreddit.title,
        'description' : subreddit.description
    }
    return data

def main():
    thread_url = 'AIethics'
    data = get_thread_data(thread_url)
    print(data)
    # assume you have a praw.Reddit instance bound to variable `reddit`


main()