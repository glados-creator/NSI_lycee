<!---------------------------------------------------- 
Fichier:  LitValeurs.php 
Description : Extraction des valeurs transmises dans 
un URL et sauvegarde dans un fichier .txt
-----------------------------------------------------?> 

<?php
	$i=0;
	// Temp, Lum et Hum sont transmises dans une url
	// Exemple : http://127.0.0.1/Grandeurs_Physiques/LitValeurs.php?Temp=20.6&Lum=1&Hum=61
	$GrandreursPhysique[0]=$_GET["Temp"];
	$GrandreursPhysique[1]=$_GET["Lum"];
	$GrandreursPhysique[2]=$_GET["Hum"];
	$Fichier_Sauvegarde = fopen("data/data.txt","w");
	
	for($i=0;$i<3;$i++)
	{
		fputs($Fichier_Sauvegarde,$GrandreursPhysique[$i]."\n");
	}	
	fclose($Fichier_Sauvegarde);		
?>
