import schedule
import time
from RedditLeaderboards import post_leaderboard

# Schedule posts for different subreddits at optimal times
schedule.every().monday.at("06:00").do(lambda: post_leaderboard("technology"))
schedule.every().tuesday.at("06:00").do(lambda: post_leaderboard("science"))
schedule.every().wednesday.at("06:00").do(lambda: post_leaderboard("gaming"))
schedule.every().thursday.at("04:00").do(lambda: post_leaderboard("news"))
schedule.every().friday.at("04:00").do(lambda: post_leaderboard("movies"))
schedule.every().saturday.at("07:00").do(lambda: post_leaderboard("funny"))
schedule.every().sunday.at("08:00").do(lambda: post_leaderboard("aww"))


print("✅ Scheduler started! The bot will post leaderboards at scheduled times.")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds

