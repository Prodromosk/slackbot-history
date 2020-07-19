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

_A simple slackbot made with python flask to populate conversations.history. Soon i will add full message history.
Unfortunately, I haven't added a correct API TOKEN but is very easy to build if you follow the readme_

*You can uncomment the following to use the export functionality:*

```# import pandas as pd```

```      
# # write the result to a file

# name_ts = datetime.datetime.now().strftime("%d-%m-%Y")
# filename = "download/extracts/" + CHANNEL + " " + name_ts + ".json"
#
# os.makedirs(os.path.dirname(filename), exist_ok=True)
#
# with open(filename, 'w', encoding='utf-8') as f:
#   json.dump(
#       replies,
#       f,
#       sort_keys=True,
#       indent=4,
#       ensure_ascii=False
#     )
#
# # Convert extract to csv
#
# df = pd.read_json (filename)
# # print(df)
# csv_filename = filename.strip('.json')
# df.to_csv (csv_filename + ".csv", index = None)
```
