
<html>
<head>
</head>
<body>
<?php
session_start();
?>


			<p> <a href="index.php?logout='1'" style="color: red;">logout</a> </p>

<?php

if(isset($_POST['binId'])){
   	$db = mysqli_connect('localhost', 'root', '', 'registration');
		$query = "SELECT * FROM bins WHERE binId=" . $_POST['binId'];
			$results = mysqli_query($db, $query);
                if(mysqli_num_rows($results) >= 1)
					
				{ 
				  $row = mysqli_fetch_assoc($results);
				$_SESSION['binId'] = $_POST['binId'];
			      $_SESSION['color'] = $row['Type'];
				  echo "<h1> Trash no : ".$_SESSION['binId']." is now active</h1>" ;
				echo "<h1>Submit when youare done  :  </h1>";
				}
				else{
	
header('location: index.php');
}
}
else{
	
header('location: index.php');
}


?>


<form action="inputTrash.php" method="POST">
<input type="text" name="color" id ="color" readonly>
<input type="submit" value="submit">
</form>






	  
      <script type = "application/javascript">
         window.onload =  function(){
            var data_file = "http://10.177.12.164:5000/800/";
            var http_request = new XMLHttpRequest();
            try{
               // Opera 8.0+, Firefox, Chrome, Safari
               http_request = new XMLHttpRequest();
            }catch (e){
               // Internet Explorer Browsers
               try{
                  http_request = new ActiveXObject("Msxml2.XMLHTTP");
					
               }catch (e) {
				
                  try{
                     http_request = new ActiveXObject("Microsoft.XMLHTTP");
                  }catch (e){
                     // Something went wrong
                     alert("Your browser broke!");
                     return false;
                  }
					
               }
            }
			
            http_request.onreadystatechange = function(){
               if (http_request.readyState == 4  ){
                  var jsonObj = JSON.parse(http_request.responseText);

                  document.getElementById("color").value = jsonObj.type;
			   }
            }
			
            http_request.open("GET", data_file, true);
            http_request.send();

		 }
		
      </script>


</body>
</html>