#  Reddit Leaderboard Bot.

A fully automated Reddit bot that posts leaderboard rankings to multiple subreddits at scheduled times. The bot fetches top contributors, formats them into a ranking system, and posts it as a Reddit post.

##  Project Structure
```
RedditBot/
│── Credentials.env             # Stores Reddit API credentials (DO NOT SHARE!)
│── RedditLeaderboards.py       # Core logic for fetching and formatting leaderboard data
│── Post_RedditLeaderboard.py   # Scheduler to automate posting at specific times
│── requirements.txt            # Dependencies for setting up the bot
│── venv/                       # Virtual environment (recommended for isolated execution)
```

## Features
✅ **Automated Leaderboard Posting** – Posts daily leaderboards to selected subreddits.  
✅ **Multiple Subreddits Support** – Customize schedules for different themes.  
✅ **Scheduled Posting** – Uses `schedule` to automate submissions at peak engagement times.  
✅ **Secure API Authentication** – Uses `.env` for secure credential storage.  
✅ **Error Handling & Logging** – Ensures smooth operation with useful debugging logs.  

##  Setup Instructions
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/RedditBot.git
cd RedditBot
```

### 2️⃣ Set Up a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Credentials
Create a `Credentials.env` file in the project directory and add your Reddit API details:
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_bot_username
REDDIT_PASSWORD=your_bot_password
REDDIT_USER_AGENT=your_custom_user_agent
```

### 5️⃣ Run the Bot
To test manually:
```bash
python Post_RedditLeaderboard.py
```
To run in the background:
```bash
nohup python Post_RedditLeaderboard.py > bot.log 2>&1 &
```

### 6️⃣ Keep the Bot Running (PythonAnywhere or Server)
- On PythonAnywhere, set up a **scheduled task**.
- On a Linux server, use `nohup` or `screen`.
- For permanent background execution:
```bash
crontab -e
# Add this line (runs the bot on reboot)
@reboot /path/to/venv/bin/python /path/to/RedditBot/Post_RedditLeaderboard.py 

```

##  How It Works
1️⃣ `RedditLeaderboards.py` fetches and formats leaderboard rankings.  
2️⃣ `Post_RedditLeaderboard.py` schedules and automates the posting.  
3️⃣ Submissions are posted based on `schedule.every().day.at("12:00").do(...)`.  
4️⃣ The bot logs activities to `bot.log` for monitoring.. 

## Default Schedule
| Subreddit  | Posting Time (UTC) |
|------------|------------------|
| `r/technology` | 12:00 PM |
| `r/fun`        | 2:00 PM  |
| *(Add More!)*  | *(Custom Time!)* |

##  Important Notes
- **Keep your `Credentials.env` file safe!** Never share it publicly.
- **Test before deploying** to ensure correct scheduling and API access.
- **Modify schedule and logic** in `Post_RedditLeaderboard.py` as needed.



---
Made with ❤️ for Reddit automation. 🚀 Happy coding!
---
### by Contractor-x
      
      In collaboration with @Ash-Cyber-and-Computer-Organizati0n............

