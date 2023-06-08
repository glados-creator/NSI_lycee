<?php
function bar_header(){
  # set session cookie
    session_name($_COOKIE['PHPSESSID']);
    session_set_cookie_params(time() + 3600,"/",$_SERVER["SERVER_NAME"],true,false);
    session_start();

# set normal html header
    echo "
<!doctype html>
<html>
  <head>
    <meta charset =\"utf-8\" />
    <link rel=\"icon\" type=\"image/x-icon\" href=\"/images/favicon.ico\">
    <link rel=\"stylesheet\" href=\"style.css\">
    <title> club informatique </title>
  </head>

  <body>
    <header>
      <img src=\"images/logo_web.png\" alt=\"Banner_logo.jpg\"/>
";

if(isset($_SESSION["USERNAME"]) && isset($_SESSION["PRENOM"])){
    # connected user 
    echo "
      
        <form action=\"compte.php\">
          <input type=\"submit\" class=\"bouttonuser\" title=\"mon compte\"
          value=\"";
    echo $_SESSION["USERNAME"];
    echo " ; ";
    echo $_SESSION["PRENOM"];
    echo "
          \">
        </form>
      
    ";
} else {
    # user not connected
    echo "
      <ul>
        <!-- not contected -->
        <li>
          <form action=\"login.php\">
            <input type=\"submit\" class=\"bouttonuser\" value=\"s'inscrire\">
          </form>
        </li>
        <li>
          <form action=\"connect.php\">
            <input type=\"submit\" class=\"bouttonuser\" value=\"se connecter\">
          </form>
        </li>
      </ul>
    ";
}
echo "</header>";
}

function bar_nav(){
  # navigation barre
  echo "
    <nav>
          <!-- home | Nos activitées | Nos inforamtions -->
          <ul>
            <li>
              <form action=\"accueil.php\">
                <input type=\"submit\" class=\"monboutton inligne\"  value=\"accueil\">
              </form>
            </li>

            <li>
              <form action=\"activite.php\">  
                <input type=\"submit\" class=\"monboutton inligne\"  value=\"Nos activitées\">
              </form>
            </li>

            <li>
              <form action=\"information.php\"> 
                <input type=\"submit\" class=\"monboutton inligne\" value=\"Nos informations \">
              </form>
            </li>
          </ul>
    </nav>
";
}

function normal(){
  echo "<section><article><fieldset>";
}

function space(){
  echo "<div><div style=\"visibility:hidden;width:1px;background:#ddd;height:0.1cm;display:inline-block;\"></div><div style=\"visibility:hidden;width:1px;background:none;height:0.1cm;display:inline-block;\"></div><div style=\"visibility:hidden;width:1px;background:red;height:0.1cm;display:inline-block;\"></div></div>";
}

function normal_end(){
  space();
  echo "</fieldset></article></section>";
}

function bar_footer(){
  space();
  space();
  echo "
    <footer>
        <h2> ce site utilise un cookie </h2>";
    if (isset($_SESSION["admin"])){
      if (boolval($_SESSION["admin"])){
        echo "<h3>(admin)</h3>";
      }
    }
        echo "
    </footer>
  </body>
</html>
  ";
}
