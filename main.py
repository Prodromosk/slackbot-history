import os
import json
import time
import datetime
from time import sleep
import pandas as pd
from flask import Flask, render_template, request, flash, redirect, url_for, Markup
from slack import WebClient
from slack.errors import SlackApiError

client = WebClient(token=os.environ["SLACK_API_TOKEN"])
MESSAGES_PER_PAGE = 200

app = Flask(__name__)

# Custom template filter for UNIX timestamp conversion to readable Date
@app.template_filter('ctime')
def nix_timestamp_conversion(s):
    return time.ctime(float(s))

@app.route("/", methods=['GET', 'POST'])
def home():

    MAX_MESSAGES = 10000

    replies = []
    total_messages = None
    error = ""
    error_msg = ""

    if request.method == 'POST':
        CHANNEL = request.form['channel']

        try:
            page = 1
            response = client.conversations_history(
                channel=CHANNEL,
                limit=MESSAGES_PER_PAGE,
            )

            assert response["ok"]
            messages_all = response['messages']
            # get additional pages if below max message and if they are any
            while len(messages_all) + MESSAGES_PER_PAGE <= MAX_MESSAGES and response['has_more']:
                page += 1
                sleep(1)   # need to wait 1 sec before next call due to rate limits
                response = client.conversations_history(
                    channel=CHANNEL,
                    limit=MESSAGES_PER_PAGE,
                    cursor=response['response_metadata']['next_cursor']
                )
                assert response["ok"]
                messages = response['messages']
                messages_all = messages_all + messages

            total_messages = "A total of {} threaded messages from channel {} have been exported to /download/extracts folder".format(
                    len(messages_all),
                    CHANNEL
            )

            for message in messages_all:
                if 'thread_ts' in message:

                    timestamp = message['thread_ts']
                    convo_replies = client.conversations_replies(
                        channel=CHANNEL,
                        ts=timestamp,
                        latest='now')
                    replies.append(convo_replies['messages'])

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

        except SlackApiError as e:
            assert e.response['ok'] is False
            assert e.response['error']
            error = e.response['ok']
            error_msg = "Slack API error: " + e.response['error']
            print(error)

    return render_template('index.html',
        replies=replies,
        total_messages=total_messages,
        error = error,
        error_msg=error_msg)

if __name__ == "__main__":
    app.run(use_reloader = True, debug = True)
