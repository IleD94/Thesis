import qi
import argparse
import sys
import requests
import time

if __name__ == "__main__":
    url='http://127.0.0.1:5000/'
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="130.251.13.116",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n")
        print("Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    tts = session.service("ALTextToSpeech")
    #time.sleep ()
    response_get = requests.get(url+'planner_launch')
    my_plan = response_get.text
    if 'recognize' in my_plan:
        print ("sono dentro")
        
    if 'say_something' in my_plan:
        print ("lallero")
        tts.say('Hello!')
    print (my_plan)
    
