#/home/pi/GPIOList.py
import RPi.GPIO as GPIO
import sys
GPIOPorts=['5V','5V','G',14,15,18,'G',23,24,'G',25,8,7,'N','G',12,'G',16,20,21,'3.3V',2,3,4,'G',17,27,22,'3.3V',10,9,11,'G','N',5,6,13,19,26,'G']
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print "<Table>",
PinSet=int(sys.argv[1])

if PinSet>0:
    PinSetting=int(sys.argv[2])
    GPIO.setup(PinSet,GPIO.OUT)
    GPIO.output(PinSet,PinSetting)
Port=0
for PortNo in GPIOPorts:
    Port=Port+1
    if Port==21:
        print "<tr>",
    if type(PortNo) is int:
        GPIO.setup(PortNo,GPIO.OUT)
        State=GPIO.input(PortNo)
        OnClick="OnClick='window.location="+'"'+"/GPIO.php?GPIO="+str(PortNo)+"&State="+str(1-State)+'"'+"' "
        if State==1:
            BackGround='00FFFF'
            ToolTip="'ON'"
        else:
            BackGround='AAAAAA'
            ToolTip="'OFF'"
    else:
        OnClick=""
        if PortNo=='5V' or PortNo=='3.3V':
            BackGround='FFFF00'
            ToolTip="'Power'"
        elif PortNo=='G':
            BackGround='555555'
            ToolTip="'Ground'"
        elif PortNo=='N':
            BackGround='FF0000'
            ToolTip="'Advanced'"
    print "<td bgcolor=",BackGround,
    print " Title=",ToolTip,
    print OnClick,">",
    print PortNo,
print "</table>"
