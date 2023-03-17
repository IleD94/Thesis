#! /usr/bin/env python3
import openai
import json
from flask import Flask, redirect, request, url_for
import time
import argparse
import os

app = Flask(__name__)
openai.organization = "org-J3uY7GUfAcfHn3nFf9J8VEW8"
openai.api_key = os.getenv("OPENAI_API_KEY")

global model


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        data = json.loads(request.data)
        print(data)
        response = openai.Completion.create(
            model=model,
            prompt=data["text"],
            max_tokens=500,
            temperature=0.6,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print (data ["text"])
        #print(response)
        with open("script_teatrale.txt", "a") as f:
                f.write(data ["text"] + "\n")
                time.sleep (0.1)
                f.write (response.choices[0].text +"\n")
                time.sleep (0.1)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result").strip()
    return result


if __name__ == "__main__":
    
    global model
    text = 'This is the server for OpenAI.'
    parser = argparse.ArgumentParser(description=text)
    # Add long and short argument
    parser.add_argument("--model", "-m", type=int, help="Sets OpenAI model")
    args = parser.parse_args()
    if not args.model:
        print("The Ada model will be used")
        model = "text-ada-001"
    else:
        if args.model == 1:
            print("The Davinci model will be used")
            model = "text-davinci-003"
        elif args.model == 2:
            print("The Curie model will be used")
            model = "text-curie-001"
        elif args.model == 3:
            print("The Babbage model will be used")
            model = "text-babbage-001"
        else:
            print("The Ada model will be used")
            model = "text-ada-001"
    app.run(host="0.0.0.0", port=5002, debug=True)