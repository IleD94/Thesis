
# coding=utf-8
import qi
import argparse
import sys
import requests
import time
import math

def face_detected (value): #esempio di callback
    print (value)

if __name__ == "__main__":
    #url='http://127.0.0.1:5000/'
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="130.251.13.106", #cambia l'ip finale
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
    motion_service=session.service ("ALMotion")
    autonomousLife_service=session.service ("ALAutonomousLife")
    posture_service=session.service ("ALRobotPosture")
    autonomousLife_service.setState("disabled")
    if not motion_service.robotIsWakeUp():
        motion_service.wakeUp()
    posture_service.goToPosture("StandInit", 1)
    memory=session.service("ALMemory")
    facedet=session.service("ALFaceDetection")
    ok=facedet.learnFace ('Alice')
    print (ok)

    print (facedet.getLearnedFacesList())

# initial_motion_service = session.service("ALMotion")
# initial_posture_service = session.service("ALRobotPosture")
# if not initial_motion_service.robotIsWakeUp():
#         initial_motion_service.wakeUp()
# initial_posture_service.goToPosture("StandInit", 0.5)

# atts = session.service("ALAnimatedSpeech")
# #voice_speed = "\\RSPD=" + str(speed) + "\\"
# configuration = {"bodyLanguageMode": "contextual"} #(o random) forse si può aggiungere un movimento specifico in caso di necessita, approfondire
# atts.say ("pss pss!", configuration)
# initial_motion_service.setAngles(["HeadPitch"], [-math.radians(35)], 0.2) #non funziona, bloccare la testa
# time.sleep (5)
# autonomousLife_service=session.service ("ALAutonomousLife")
# set_autonomous_abilities(True, True, True, True, True)
# facedetected = memory.subscriber("FaceDetected") #questo permette la callback
# connection = facedetected.signal.connect(face_detected) #segnale della sottoscrizione
# face_det=memory.getData("FaceDetected")
# time.sleep (10)
    
