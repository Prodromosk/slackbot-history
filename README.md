# Ari-Slack-Bot

### To get the channel ID:
- Go to your_workspace.slack.com
- Click on the channel you want
- Copy the channel ID from the address bar

### To create the BOT:
- Create a [Slacka app](https://api.slack.com/apps/new)
- Click the OAuth & Permissions tab in the left sidebar.
- Below Bot Token Scopes, select one or more scopes. Then click Add an OAuth Scope.
- Click the App Home tab in the left sidebar to view the bot user and the configuration you’ve added.

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
- *Export SLACK_API_TOKEN="Bot User OAuth Access Token"*
- python main.py
