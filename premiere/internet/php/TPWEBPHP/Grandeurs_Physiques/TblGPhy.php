<!doctype html>
<html lang="fr">

<head>
	<meta charset="utf-8">
	<title> Affichage de grandeurs physiques </title>
	<link rel="stylesheet" href="styles/style.css">	
  </head>

<body>
<?php // Ouverture du fichier contenant les données
	$FValeur = fopen("data/data.txt","r"); 
?>
  <div>
	<p> Grandeurs physiques </p>
	<table border='1'>
		<tr>
			<td> Température =  </td>
			<td>
			<?php
				$Temp = fgets($FValeur,10); // $Temp <- première valeur de $FValeur
				echo "$Temp"; // Affichage de la valeur mémorisée dans $Temp
			?>	   
			</td>
			<td> °C </td>
		</tr>
		<!-- A compléter -->
	</table>
 </div> 
 <?php // Fermeture du fichier contenant les données
	fclose($FValeur); 
?> 

</body>

</html>