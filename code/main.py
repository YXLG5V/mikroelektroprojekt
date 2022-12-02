import os
import glob
import time
import RPi.GPIO as GPIO
import redis

BLUE_LED = 19
GREEN_LED = 13
CHANGE = True
DATA = {"celsius": 0, "farenheit": 0, "status": "LOW/HIGH"}
stream_name = 'mystream'
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
db = redis.Redis("localhost")

GPIO.setmode(GPIO.BCM)
GPIO.setup(BLUE_LED,GPIO.OUT)
GPIO.setup(GREEN_LED,GPIO.OUT)
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

while True:
    time.sleep(1)
    DATA["celsius"],DATA["farenheit"] = read_temp()
    if DATA["celsius"] < 25:
        if DATA["status"] !="LOW":
            DATA["status"]="LOW"
            CHANGE= True
    else:
        if DATA["status"] !="HIGH":
            DATA["status"]="HIGH"
            CHANGE= True
    db.xadd(stream_name, DATA, id='*')
    print("Temperature: ",DATA["celsius"], "C° Status: ",DATA["status"])
    if CHANGE:
        print("STATUS has changed to ",DATA["status"],"!")
        CHANGE = False
        if DATA["status"] =="HIGH":
            GPIO.output(BLUE_LED, GPIO.LOW)
            GPIO.output(GREEN_LED, GPIO.HIGH)
        else:
            GPIO.output(BLUE_LED, GPIO.HIGH)
            GPIO.output(GREEN_LED, GPIO.LOW)