<?php
function com_Hstart(){
    echo "
<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset =\"utf-8\" />
    <meta name=\"viewport\">
    <link rel=\"icon\" type=\"image/x-icon\" href=\"/images/favicon.ico\">
    <link rel=\"stylesheet\" href=\"style.css\">
    <title> Network simulator </title>
  </head>

  <body>
    <header>
      <fieldset>
        <nav class=\"nopad\">
          <ol class=\"nopad\">
            <li class=\"nopad\">
              <img src=\"images/logo.png\" alt=\"logo.png\" style=\"visibility: visible;\"/>
            </li>
            <li>
              <h2 class=\"center center-vertical\">Network<br>Simulation</h2>
            </li>

          <!-- home | sim | info -->
            
            <li>
              <form action=\"home.php\" class=\"nopad\">
                  <input type=\"submit\" class=\"monboutton inligne\"  value=\"accueil\">
              </form>
            </li>

            <li>
              <form action=\"sim.php\" class=\"nopad\">  
                  <input type=\"submit\" class=\"monboutton inligne\"  value=\"Simulation\">
              </form>
            </li>

            <li>
              <form action=\"info.php\" class=\"nopad\">  
                  <input type=\"submit\" class=\"monboutton inligne\"  value=\"Information\">
              </form>
            </li>
          </ol>
        </nav>
      </fieldset>
    </header>
";
}

function com_space(){
  echo "<div class=\"space\"><div class=\"space\"></div><div class=\"space\"></div><div class=\"space\"></div></div>";
}

function com_Sstart(){
  com_space();
  echo "<section><article><fieldset>";
}

function com_Send(){
  com_space();
  echo "</fieldset></article></section>";
  com_space();
}

function com_Hend(){
  com_space();
  echo "
    <footer>
      <h3>Network Simulation</h3>
      <h3>All Right Reserved</h3>
      <!-- <h3> ce site utilise un cookie </h3> -->
    </footer>";
  com_space();
  echo "
  </body>
</html>
  ";
}
?>