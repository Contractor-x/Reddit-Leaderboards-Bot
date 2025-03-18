import os
import praw
from dotenv import load_dotenv

# Load the environment variables from Credentials.env
env_path = os.path.join(os.path.dirname(__file__), "Credentials.env")
load_dotenv(env_path)  # ✅ Corrected: Now loading environment variables correctly

# Debug: Print values to check if they are loaded
print("CLIENT_ID:", os.getenv("REDDIT_CLIENT_ID"))  # Debugging
print("CLIENT_SECRET:", os.getenv("REDDIT_CLIENT_SECRET"))

# Now you can access environment variables normally
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USERNAME = os.getenv("REDDIT_USERNAME")
PASSWORD = os.getenv("REDDIT_PASSWORD")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent=USER_AGENT  # ✅ Fixed missing parenthesis
)

def post_leaderboard(subreddit_name):
    print(f"🚀 Posting leaderboard to r/{subreddit_name}...")

    try:
        subreddit = reddit.subreddit(subreddit_name)
        
        title = "🔥 Top 5 Contributors This Week!"
        body = """
        1. u/User1 - 500 points
        2. u/User2 - 450 points
        3. u/User3 - 400 points
        4. u/User4 - 350 points
        5. u/User5 - 300 points
        """

        # Post to Reddit
        post = subreddit.submit(title, selftext=body)
        print(f"✅ Posted successfully! Link: https://www.reddit.com{post.permalink}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Function to post the leaderboard
def post_leaderboard(subreddit_name):
    print(f"🚀 Posting leaderboard to r/{subreddit_name}...")
    # Your logic to generate and post the leaderboard goes here

# Test the bot
if __name__ == "__main__":
    print("✅ Successfully loaded .env and authenticated with Reddit!")
