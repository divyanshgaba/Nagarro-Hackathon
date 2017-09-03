<?php 
	session_start(); 

	if (!isset($_SESSION['username'])) {
		$_SESSION['msg'] = "You must log in first";
		header('location: login.php');
	}

	if (isset($_GET['logout'])) {
		session_destroy();
		unset($_SESSION['username']);
        unset($_SESSION['id']);
		header("location: login.php");
	}

?>
<!DOCTYPE html>
<html>
<head>
	<title>Home</title>
	<link rel="stylesheet" type="text/css" href="style.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
<header>
		<?php  if (isset($_SESSION['username'])) : ?>
			<p>Welcome <strong><?php echo $_SESSION['username'] ; ?></strong></p>
			<p> <a href="index.php?logout='1'" style="color: red;">logout</a> </p>
		<?php endif ?>
		</header>
	<div class="header">
		<h2>Home Page</h2>
	</div>
	<div class="content">

		<!-- notification message -->
		<?php if (isset($_SESSION['success'])) : ?>
			<div class="error success" >
				<h3>
					<?php 
						echo $_SESSION['success']; 
						unset($_SESSION['success']);
					?>
				
				</h3>


		</div>
		<?php endif ?>

		<!-- logged in user information -->

<div>
		<form method="POST" action="binActive.php">
           		<div class="input-group">
			<label> Enter Bin Id </label>
			<input type="text" name="binId" >
		</div>
              <div class = "input-group">
			<input type="submit" value="submit">
		</div>
	</form>			  
</div>	
	<?php
		$db = mysqli_connect('localhost', 'root', '', 'registration');
		$query = "SELECT * FROM trash WHERE UserId=" . $_SESSION['id'];
			$results = mysqli_query($db, $query);
                if(mysqli_num_rows($results) >= 1)
				{  echo " <table>
						<thead>
						<tr>
						  <th>BIN ID </th>
						  <th>Points</th>
						 </tr>
						 </thead>
						 <tbody>
						 ";
					$totalPoints= 0;
                    while($row = mysqli_fetch_assoc($results))
					{  echo "<tr> 
				             <td>".
							 $row["BinId"]."</td><td>".$row["Points"]."</td></tr>";
					$totalPoints +=$row["Points"]; 	
					}
				    echo "</tbody></table>";
				}
                 echo"<h3> Your total points are : ". $totalPoints;
				?>
	
</div>
	
<ul>
<li><img src="images/amazon.jpg" height = "150" width = "150" ></li>
<li><img src="images/bms.png"height = "150" width = "150"></li>
<li><img src="images/ola.png" height = "150" width = "150"></li>
<li><img src="images/paytm.jpg" height = "150" width = "150"></li>


</ul>




</body>
</html>