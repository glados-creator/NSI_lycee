<?php
include_once("common.php");
com_Hstart();
com_Sstart();

echo "<h1 class=\"center\">accueil</h1>
<h3 class=\"center\">ce site simule un réseau</h3>
<h3 class=\"center\">placer différente node dans le canvas</h3>
<h3 class=\"center\">clicker dans la liste pour modifier leurs attribut</h3>
<h3 class=\"center\">le seul protocole implementer est le ping</h3>
<h3 class=\"center\">plus de protocole a venir dans le futur</h3>";

com_Send();
com_Hend();
?>