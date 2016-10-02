#/home/pi/GPIOLang.py
import RPi.GPIO as GPIO
import sys
import time

def GroupSwitch(PinArray,Setting):
    for PinNo in PinArray:
        GPIO.output(PinNo,Setting)


GPIOPorts=[14,15,18,23,24,25,8,7,12,16,20,21,2,3,4,17,27,22,10,9,11,5,6,13,19,26]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
FirstParam=True
for PinNo in GPIOPorts:
    GPIO.setup(PinNo,GPIO.OUT)
  
for Command in sys.argv:
    if FirstParam:
        GroupSwitch (GPIOPorts,0)
        FirstParam=False
    else:
        param=Command[3:]
        Cmd=Command[:3]
        print Cmd
        print param
 
        if Cmd=='Dly':
            time.sleep (float(param))
        elif Cmd=='TEO':
            GroupSwitch (GPIOPorts,0)
        elif Cmd=='On-':
            exec("TempArray=["+param+"]")
            GroupSwitch (TempArray,1)
        elif Cmd=="Off":
            exec("TempArray=["+param+"]")
            GroupSwitch (TempArray,0)

