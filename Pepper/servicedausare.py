---------------------> sta parte si può usare nel main, ma non è detto che io faccia due classi
# ---------   PER SETTARE IL ROBOT NELLA POSIZIONE INIZIALE  ------------
initial_motion_service = session.service("ALMotion")
initial_posture_service = session.service("ALRobotPosture")
if not initial_motion_service.robotIsWakeUp():
        initial_motion_service.wakeUp()
initial_posture_service.goToPosture("StandInit", 0.5) # ce ne sono anche altre


# ---------- PER SETTARE IL VOLUME, UTILE PER ALCUNE AZIONI ------
volume = 60 # il valore massimo, poi lo abbassiamo quando deve sparlare
audio = session.service("ALAudioDevice")
audio.setOutputVolume(volume) 


# --------- EVENTI DA SETTARE NEL THREAD DEI SENSORI PER KILLARLO
import threading
kill_event = threading.Event()

# --------- classe per gestire le code prendendo prima sempre l'ultimo dato
from Queue import LifoQueue
q = LifoQueue() 

# -------- come chiamare il thread dei sensori con i suoi flag ------
from sensorsT import SensorsThread
sensors=SensorsThread(session, queue=q, kill_event=kill_event)
sensors.name = "Sensors_thread"
sensors.daemon = True # in questo modo lo si rende un demone
sensors.start () # questo si usa per inizializzare il tread
##### LASCIARE DEI SECONDI PERCHE' I SENSORI SI AVVIINO CORRETTAMENTE

# ------- Quando voglio killare il mio thread dei sensori posso scriveree
kill_event.set()
sensors.join() #aspetta che il thread dei sensori si chiuda prima di ricominciare
# si può usare in un try- except KeyboardInterrupt, dentro l'except si killa e si joina
KeyboardInterrupt #se viene premuto ctrl-c

# -------------------------------------------------------------------------------------------
self.set_autonomous_abilities(True, True, True, True, True)
def set_autonomous_abilities(self, blinking, background, awareness, listening, speaking):
        self.al.setAutonomousAbilityEnabled("AutonomousBlinking", blinking)
        self.al.setAutonomousAbilityEnabled("BackgroundMovement", background)
        self.al.setAutonomousAbilityEnabled("BasicAwareness", awareness)
        self.al.setAutonomousAbilityEnabled("ListeningMovement", listening)
        self.al.setAutonomousAbilityEnabled("SpeakingMovement", speaking)

# -------------------------ESEMPIO DI CALLBACK --------------------------------------
self.end_of_sentence = self.memory.subscriber("FaceDetected") qui il nome dell'evento
    self.end_of_sentence.signal.connect(self.on_sentence_over) dentro si mette la callback

 # for i in range (len (myfriends)):
        #     if myfriends[i] in people:
        #         counter[i]+=1

        # time.sleep (1)
        face_detection_data=self.memory.getData("FaceDetected")
        if len(face_detection_data)>1:
            faceInfoArray=face_detection_data[1][0]
            print (faceInfoArray[1][2])