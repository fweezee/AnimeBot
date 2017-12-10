from slackclient import SlackClient
import time
import os
from Brain import Brain

token = ("xoxb-283130767090-E1h0FByYRdwDgZWV127GtwUl")

slack_client = SlackClient(token)

link = '<https://cdn.meme.am/instances/400x/33568413.jpg|That would be great>'

recommend = ['recommend', 'suggest']
greetings = ['hi', 'hello', 'ohayo']
search = ['what anime', 'search', 'find', 'look for']


def replyGenerator(text):
    return "NICE"


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

                # if 'recommend' in text.lower() and link not in text:
                #     slack_client.api_call(
                #         'chat.postMessage',
                #         channel=channel,
                #         text="gladdly",
                #         as_user='true:'
                #     )


                # if any(word in text.lower() for word in recommend):
                #     slack_client.api_call(
                #         'chat.postMessage',
                #         channel=channel,
                #         text=Brain.suggest(text),
                #          as_user='true:'
                #     )

                if any(word in text.lower() for word in search):

                    newText = text

                    for temp in search:
                        newText = newText.replace(temp + " ", "")

                    print(newText)

                    slack_client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text=Brain.searchData(newText),
                         as_user='true:'
                    )

                #
                # if any(word in text.lower() for word in greetings):
                #     slack_client.api_call(
                #         'chat.postMessage',
                #         channel=channel,
                #         text=Brain.suggest(text),
                #          as_user='true:'
                #     )






        time.sleep(1)
else:
    print('Connection failed, invalid token?')

