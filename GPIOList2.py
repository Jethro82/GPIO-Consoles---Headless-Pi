#/home/pi/GPIOList2.py
GPIOPorts=['5V','5V','G',14,15,18,'G',23,24,'G',25,8,7,'N','G',12,'G',16,20,21,'3.3V',2,3,4,'G',17,27,22,'3.3V',10,9,11,'G','N',5,6,13,19,26,'G']

print "<Table border=1>",

Port=0
SequentialPinNo=0
for PortNo in GPIOPorts:
    Port=Port+1
    if Port==21:
        print "<tr>",
    if type(PortNo) is int:
            BackGround='FFFFFF'
            ToolTip="GPIO "+str(PortNo)
            CheckBox="<input type='checkbox' id='GPIO"+str(SequentialPinNo)+"' name='"+str(PortNo)+"'>"
            SequentialPinNo+=1

    else:
        CheckBox=""
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
    print " Title=",ToolTip,">",
    print CheckBox,
    print PortNo,
print "</table>"
