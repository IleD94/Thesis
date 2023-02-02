
import qi
import argparse
import sys
import requests
import time
from fsm import StateMachine


if __name__ == "__main__":

    # create an instance of the state machine class
    machine = StateMachine()
    # start in state one
    machine.current_state = "state_zero"

    # loop forever
    ret=True
    while ret:
        # get the method for the current state
        state_method = getattr(machine, machine.current_state)
        # call the method
        state_method()
#exit(0)