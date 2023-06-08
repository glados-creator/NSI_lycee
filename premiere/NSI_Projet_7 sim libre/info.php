<?php
include_once("common.php");
com_Hstart();
com_Sstart();

echo "<h1 class=\"center\">information</h1>
<h3 class=\"center\">ce site simule un réseau</h3>
<h3 class=\"center\">placer différente node dans le canvas</h3>
<h3 class=\"center\">une réticule va la ou vous clicker</h3>
<h3 class=\"center\">selectioner et après ajouter a l'endroit de la réticule</h3>
<h3 class=\"center\">menu des différent composants disponible : </h3>
<ul>
</li>ordinateur - computer</li>
</li>téléphone - phone</li>
</li>router</li>
</li>switch</li>
</li>ordinateur portable - laptop</li>
</li>wireless - point d'accès wifi</li>
</ul>
<h3 class=\"center\">clicker dans la liste pour modifier leurs attribut</h3>
<h3 class=\"center\">le seul protocole implementer est le ping</h3>
<h3 class=\"center\">il n'y a pas encore de vérification pour ne pas que 2 appareils ont la meme addresse ip</h3>
<h3 class=\"center\">plus de protocole a venir dans le futur</h3>
<h3 class=\"center\">debug mode pour modifier les attribut \"rule\" comme vous le voulez</h3>
<h3 class=\"center\">il manque la partie js pour ajouter des connection</h3>
<h3 class=\"center\">il manque la partie js pour modifier la partie select avec la var select</h3>
<h3 class=\"center\">qui est senser montrer mes attribut de l'objet</h3>
<h3 class=\"center\">il manque la partie html pour proprement montrer les menus</h3>
<h3 class=\"center\">Crédit : PAVARD Arthur</h3>
";

com_Send();
com_Hend();
?>