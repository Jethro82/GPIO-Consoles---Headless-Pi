<Title>GPIO Console Control(Basic Output)</Title>
GPIO Console Control - Basic Output mode
<?php
	$PinNo=$_GET['GPIO'];
	if ($PinNo>1){
		$State=$_GET['State'];
		if (($State==0) or ($State==1)){
			$Exec='python /home/pi/GPIOList.py '.$PinNo.' '.$State;
		}
	}else{

		$Exec='python /home/pi/GPIOList.py 0';
	}
	echo exec($Exec);
?>