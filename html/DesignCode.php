
<?php
	echo $_GET['Code'];
	if (isset($_POST['Code'])){
		$Code=str_replace(" ","",$_POST['Code']);
		$Code=str_replace("\n"," ",$Code);
		$Code=str_replace(" -"," ",$Code); // Ensure no switch parameters are sent to python in super user mode
		shell_exec('python /home/pi/GPIOLang.py '.$Code.'> /dev/null 2>/dev/null &');
		echo '<br>Running Code... (This may take a while)<br>';
	}
	echo 'Change pins:';
	echo exec('python /home/pi/GPIOList2.py');
	echo 'to ';
	echo '<select id="OnOff">'.
	 '<option value="On-">On'.
	 '<option value="Off">Off</select>'.
	 'and wait for '.
	 '<select id="Delay">';
	for ($seconds=0; $seconds<60; $seconds+=1){
		echo '<option value="'.$seconds.'">'.$seconds;
	}
	echo '</select> seconds<br>';
	echo '<button onclick="SwitchCommand()">Add Instruction</button>';
	echo '<button onclick="TEO()">Turn Everything Off</button><br>';
	echo '<form action="DesignCode.php" method="post">';
	echo "<textarea name='Code' row='20' columns='25' id='Code'>";
	if (isset($_POST['Code'])){
		echo $_POST['Code'];
	}
	echo '</textarea>';
	echo '<br><input type="Submit" value="Run"></form>';
?>

<Script>
function TEO(){
	document.getElementById("Code").value+="TEO\n";
}
function SwitchCommand() {
	appendtext=document.getElementById('OnOff').value;

	AddedBox=false;
	for(CBoxNo=0; CBoxNo<26; CBoxNo+=1){
		if (document.getElementById("GPIO"+CBoxNo).checked==true){
			if(AddedBox==true){
				appendtext+=',';
			}
			AddedBox=true;
			appendtext+=document.getElementById("GPIO"+CBoxNo).name;
		}
		document.getElementById("GPIO"+CBoxNo).checked=false;
	}
	appendtext+="\n";
	if (document.getElementById("Delay").value>0){
		appendtext+="Dly";
		appendtext+=document.getElementById("Delay").value;
		appendtext+="\n";
	}
	document.getElementById("Code").value+=appendtext;
}
</Script>