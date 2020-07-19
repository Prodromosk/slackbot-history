# RPA-Slack-Bot

### export SLACK_API_TOKEN="Bot User OAuth Access Token"
### export CHANNEL_TO_LISTEN="THE CHANNEL ID YOU WANT TO LISTEN"

### To get the channel ID:
- Go to your_workspace.slack.com
- Click on the channel you want
- Copy the channel ID from the address bar

#### Make sure the bot is invited to the channel you want to listen.
#### Make sure you provide the following bot token scopes:
- channels:history
- channels:read
- groups:history
- im:history
- mpim:history

## Getting started
- Clone or download the repo 
- pip install -r requirements.txt
- python app.py
