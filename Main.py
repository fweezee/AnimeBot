from slackclient import SlackClient
import time
import os

token = ("xoxb-283130767090-bY8Sw1ZkHNGGjtiuJsEj5U63")

slack_client = SlackClient(token)

link = '<https://cdn.meme.am/instances/400x/33568413.jpg|That would be great>'

def speechAnalysis(text):
    return text



def replyGenerator(text, channel):

    if 'do what' in text.lower() and link not in text:
        slack_client.api_call(
            'chat.postMessage',
            channel=channel,
            text=link,
            as_user='true:'
        )

    if 'suck my dick' in text.lower() and link not in text:
        slack_client.api_call(
            'chat.postMessage',
            channel=channel,
            text="gladdly",
            as_user='true:'
        )



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

                replyGenerator(text, channel)
        time.sleep(1)
else:
    print('Connection failed, invalid token?')

