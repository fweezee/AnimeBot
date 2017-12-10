from slackclient import SlackClient
from Speech import Speech
import time
import os

token = ("xoxb-283130767090-bY8Sw1ZkHNGGjtiuJsEj5U63")

slack_client = SlackClient(token)

link = '<https://cdn.meme.am/instances/400x/33568413.jpg|That would be great>'



def replyGenerator(text, channel):
    Speech.speechAnalysis(text)



if slack_client.rtm_connect():
    print("Connected!!!!")
    while True:
        events = slack_client.rtm_read()
        for event in events:
            if (
                'channel' in event and
                'text' in event and
                event.get('type') == 'message'
            ):
                channel = event['channel']
                text = event['text']

                # if 'do what' in text.lower() and link not in text:
                #     slack_client.api_call(
                #         'chat.postMessage',
                #         channel=channel,
                #         text=link,
                #         as_user='true:'
                #     )
                #
                # if 'suck my dick' in text.lower() and link not in text:
                #     slack_client.api_call(
                #         'chat.postMessage',
                #         channel=channel,
                #         text="gladdly",
                #         as_user='true:'
                #     )

                slack_client.api_call(
                    'chat.postMessage',
                    channel=channel,
                    text=replyGenerator(text,channel),
                    as_user='true:'
                )

        time.sleep(1)
else:
    print('Connection failed, invalid token?')

