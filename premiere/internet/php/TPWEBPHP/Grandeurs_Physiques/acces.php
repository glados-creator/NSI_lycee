<?php 
	if (($_GET["login"] == "admin") && ($_GET["motpasse"] == "1234"))
		{ 
			header('Location: TblGPhy.php');
		}
	else
			echo "Acces refusé";
?>