import functions
import qi
import argparse
import sys
import requests
import time
from state_machine import StateMachine
from sensorsT import SensorsThread
from Queue import LifoQueue
import threading
import getcurrentstate
import zmq

predicates_to_check=None
predicates= None
stablepred=None
myobj1=None



def functions_print ():
    print (stablepred)
    print ("\n")
    print (predicates)
    print ("\n")
    print (predicates_to_check)
    print ("\n")
    print (myobj1)

def set_autonomous_abilities(al, blinking, background, awareness, listening, speaking):
    al.setAutonomousAbilityEnabled("AutonomousBlinking", blinking)
    al.setAutonomousAbilityEnabled("BackgroundMovement", background)
    al.setAutonomousAbilityEnabled("BasicAwareness", awareness)
    al.setAutonomousAbilityEnabled("ListeningMovement", listening)
    al.setAutonomousAbilityEnabled("SpeakingMovement", speaking)

if __name__ == "__main__":

 #PEPPER INITIALIZATION
    url='http://127.0.0.1:5005/'
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="130.251.13.106",
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

    #SERVICE FOR THE PROGRAM
    motion_service=session.service ("ALMotion")
    autonomousLife_service=session.service ("ALAutonomousLife")
    posture_service=session.service ("ALRobotPosture")
    
    
    
    #INITIAL STATE
    autonomousLife_service.setState("disabled")
    if not motion_service.robotIsWakeUp():
        motion_service.wakeUp()
    posture_service.goToPosture("StandInit", 1)
    motion_service.setStiffnesses("Head", 1.0)
    motion_service.setAngles("Head", [0.0, 0.0], 0.1)
    #motion_service.setAngles("HeadYaw", 0, 0.5) 
    posture_service.stopMove()
    set_autonomous_abilities(autonomousLife_service, False, False, False, False, False)
    time.sleep (1)
    # start sensors thread, queue and kill_event
    kill_event = threading.Event ()
    #q = LifoQueue()
    lock = threading.Lock()
    sensors=SensorsThread(session, lock=lock, kill_event=kill_event )
    sensors.name = "Sensors_thread"
    sensors.daemon = True
    sensors.start ()
    time.sleep (1) # tempo di avviamento dei sensori
    
    # if KeyboardInterrupt:
    #     kill_event.set()
    #     sensors.join ()
    #     print ("Session terminated")

    
    #time.sleep(60)
    
    
    predicates_to_check = sensors.predicates_to_check
    #queue1.put(predicates)
    stablepred = sensors.stablepred

    predicates = sensors.predicates
    myobj1 = sensors.myobj1

    while myobj1 == []:
        time.sleep(0.1)
        myobj1 = sensors.myobj1
    #functions_print ()
    print (myobj1)
    goal = functions.socket_goal_exchange()
    functions.write_pddl(predicates, goal, myobj1)
    expected_effects_list, expected_precondition_list, actions, my_plan_splitted =getcurrentstate.start()

    #print (expected_effects_list)
    # create an instance of the state machine class
    if my_plan_splitted == []:
        current_state = "state_one"
    else:
    # # start in state one
        current_state = "state_three"
        
    machine = StateMachine(session, predicates_to_check, stablepred, expected_effects_list, expected_precondition_list, actions, my_plan_splitted, lock=lock, current_state=current_state)
    
    
    # # loop forever
    my_condition = True
    while my_condition:
    #     # get the method for the current state
        state_method = getattr(machine, machine.current_state)
    #     # call the method
        state_method()
        if machine.done:
            my_condition = False
    
    kill_event.set()
    sensors.join ()
    exit(0)


