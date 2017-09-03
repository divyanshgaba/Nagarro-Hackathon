<?php
session_start();
?>

			<p> <a href="index.php?logout='1'" style="color: red;">logout</a> </p>

<?php

$var=0;
   if($_SESSION['color']==$_POST['color'])
	   $var = 20;
   
	$db = mysqli_connect('localhost', 'root', '', 'registration');
		$query = "insert into trash values (" . $_SESSION['id'] . "," . $_SESSION['binId']  .  ",".$var .")";
			$results = mysqli_query($db, $query);
   
header('Location: index.php');

?>