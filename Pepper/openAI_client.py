import json
import requests
import argparse
import time


def req(text):
    data = json.dumps({'text': text})
    start_time = time.time()
    res = requests.post("http://127.0.0.1:5002/", data=data)
    end_time = time.time()
    print(res.text)
    print(end_time-start_time)
    return res.text


# Press the green button in the gutter to run the script.
def start (language, personality, action_in_natural_languange):
    description = 'This is the server for OpenAI.'
    # parser = argparse.ArgumentParser(description=description)
    # # Add long and short argument
    # parser.add_argument("--sentence", "-s", help="Input text")
    # args = parser.parse_args()
    # if not args.sentence:
    #     sentence = "dimmi qualcosa"
    # else:
    #     sentence = args.sentence
    sentence = "Create an " + language + " sentence of about 35 words in a " + personality + " tone in which you " + action_in_natural_languange
    res = req(sentence)
    return  res
