import os
import praw
from dotenv import load_dotenv

# Load API keys
load_dotenv()

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USERNAME = os.getenv("REDDIT_USERNAME")
PASSWORD = os.getenv("REDDIT_PASSWORD")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD
)

def fetch_trending_posts(subreddit_name="all", limit=5):
    """Fetch top trending posts from a subreddit."""
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = subreddit.hot(limit=limit)  # Get 'hot' posts

    leaderboard = []
    for post in top_posts:
        leaderboard.append(f"**[{post.title}]({post.url})** (⬆ {post.score} | 💬 {post.num_comments})")
    
    return "\n\n".join(leaderboard)

def post_leaderboard(subreddit_name="test"):
    """Post the leaderboard to a subreddit."""
    leaderboard_text = fetch_trending_posts(subreddit_name)
    
    title = f"🔥 {subreddit_name.capitalize()} Top Posts Leaderboard"
    body = f"📢 Here are the **top trending posts** from r/{subreddit_name} today:\n\n{leaderboard_text}\n\n---\n*🤖 This post was made by a bot.*"

    # Post to subreddit
    subreddit = reddit.subreddit(subreddit_name)
    subreddit.submit(title, selftext=body)
    
    print(f"✅ Posted leaderboard to r/{subreddit_name}")

# Test posting to a test subreddit
if __name__ == "__main__":
    post_leaderboard("test")
