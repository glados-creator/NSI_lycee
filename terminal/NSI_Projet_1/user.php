<?php
session_start();
$servername = "localhost";
$username = "root";
$password = "";

/// destroy session
function Disconnect_user(){
    session_unset();
    session_destroy();
    echo "<h3>user disconnected</h3>";
    echo "<meta http-equiv='Refresh' content='0; url=/' />";
}

function failS($e){
    echo "
    <div class='center' style='background-color: red;'>
        <h3>Erreur d'une partie SQL</h3>
        <h3>";
        echo $e;
        echo "</h3>
    </div>";
    die();
}

function SQLinsert($conn ,$sql){
    if (mysqli_query($conn, $sql)) {
      mysqli_insert_id($conn);
    } else {
      throw new Exception("Error: " . $sql . "<br>" . mysqli_error($conn));
    }
}

function SQLselect($conn ,$sql){
    $result = mysqli_query($conn, $sql);
    if (mysqli_num_rows($result) > 0) {
      // output data of each row
      $r =array();
      while($row = mysqli_fetch_assoc($result)) {
        array_push($r,$row);
      }
      return $r;
    } else {
      return array();
    }
}

function SQLcom($conn ,$sql){
    if (mysqli_query($conn,$sql)) {
    } else {
        failS($conn->error);
    }
}

function SQLCoServe($func){
    global $servername, $username, $password;
    /// se co au serve 
    try {
        /// opti potanciel -> mettre $conn dans $_session
        /// et le fermer que quand on se déconnect
        /// mais les gens ne se déconnecte pas donc il faudrai vérifier 
        /// les session et fermer $conn avec une session
        /// hors du scope
        $conn = mysqli_connect($servername, $username, $password);
        if ($conn->connect_error) {
            throw new Exception($conn->connect_error);
        }
        SQLcom($conn,"use motel");
        $func($conn);
        mysqli_close($conn);
    }
    catch (Exception $e){
        failS($e->getMessage());
    }
}

/// Connect a user
function Connect_User($conn){
    if ($_GET["username"] == "admin" && $_GET["password"] == "123456789"){
    $_SESSION["admin"] = True;}
    echo "<h3>user connected</h3>";
    SQLCoServe(function ($conn){
        $id = SQLselect($conn,"select Idclient from client where Cusername='".$_GET["username"]."' and Cpassword='".md5($_GET["password"])."'"); 
        if (count($id) != 1){
            throw new Exception("no user");
        }
        $_SESSION["id"] = intval($id[0]["Idclient"]);
    });
    unset($_GET["dispatch"]);
    $_SESSION["order_c"] = array();
    $_SESSION["sql"] = "select DISTINCT * from client join relation on client.Idclient=relation.IdCB and relation.IdCA=".$_SESSION["id"];
    echo "<meta http-equiv='refresh' content='0; url=/user.php'/>";
}

/// add user
function Creat_user($conn){
    $max_id = SQLselect($conn,"select count(*) from client;");
    $max_id = intval($max_id[0]["count(*)"]);
    $max_id = $max_id + 1;
    SQLinsert($conn,"insert into client 
    (`Idclient`,`Cnom`,`Cprenom`,`Cusername`,`Cpassword`,`Cdateborn`,`Cadresse`,`Cprofession`,`Cpublic`,`Cnumtelfixe`,`Cnumtelport`,`Cemail`) values (". $max_id ." , '".$_GET["nom"]."','".$_GET["prenom"]."','".$_GET["username"]."','". md5($_GET["password"]) ."','".$_GET["born"]."','".$_GET["addresse"]."','".$_GET["profession"]."',0,'".$_GET["telfix"]."','".$_GET["telport"]."','".$_GET["email"]."');");
    echo "<meta http-equiv='Refresh' content='0; url=/' />";
}

function sort_help($c){
    echo "<form action='user.php' method='GET'>";
    echo "    <input type='hidden' name='dispatch' value='app_order_up'/>";
    echo "    <input type='hidden' name='oder' value='".$c."'>";
    echo "    <input type='submit' value=&uarr;>";
    echo "</form>";
    echo "<form action='user.php' method='GET'>";
    echo "    <input type='hidden' name='dispatch' value='app_order_down'/>";
    echo "    <input type='hidden' name='oder' value='".$c."'>";
    echo "    <input type='submit' value=&darr;>";
    echo "</form>";
}

/// board print
function Get_board($b){

    /// print table keys
    /// ----------------------------------------------------------------------------------------------------
    /// (Idclient) | nom | prenom | adresse | Cprofession | numtelfixe | numtelport | email | public | tag |
    /// ----------------------------------------------------------------------------------------------------
    echo "<table><tr>";
    if (isset($_SESSION["admin"])){
    echo "<th>Idclient</th>";}
    echo "<th>nom";
    sort_help("nom");
    echo "</th>";
    echo "<th>prenom";
    sort_help("prenom");
    echo "</th>";
    echo "<th>adresse";
    sort_help("adresse");
    echo "</th>";
    echo "<th>profession";
    sort_help("profession");
    echo "</th>";
    echo "<th>numtelfixe";
    sort_help("numtelfixe");
    echo "</th>";
    echo "<th>numtelport";
    sort_help("numtelport");
    echo "</th>";
    echo "<th>email";
    sort_help("email");
    echo "</th>";
    echo "<th>tag</th><th>forme tag</th>";
    echo "</tr>";
    for ($i = 0; $i < count($b); $i++){
        /// (`Idclient`,`Cnom`,`Cprenom`,`Cusername`,`Cpassword`,`Cdateborn`,`Cadresse`,`Cprofession`,`Cpublic`,`Cnumtelfixe`,`Cnumtelport`,`Cemail`)
        echo "<tr>";
        if (isset($_SESSION["admin"])){
        echo "<td>".$b[$i]["Idclient"]."</td>";
        }
        echo "<td>".$b[$i]["Cnom"]."</td>";
        echo "<td>".$b[$i]["Cprenom"]."</td>";
        echo "<td>".$b[$i]["Cadresse"]."</td>";
        echo "<td>".$b[$i]["Cprofession"]."</td>";
        echo "<td>".$b[$i]["Cnumtelfixe"]."</td>";
        echo "<td>".$b[$i]["Cnumtelport"]."</td>";
        echo "<td>".$b[$i]["Cemail"]."</td>";
        echo "<td>";
        $_SESSION["TIdR"] = $b[$i]["IdR"];
        $_SESSION["Toptions"] = array();
        SQLCoServe(function ($conn){
            $_SESSION["Toptions"] = SQLselect($conn,"select TagR from relation where IdR='".$_SESSION["TIdR"]."'");
        });
        $Toptions = explode(";",$_SESSION["Toptions"][0]["TagR"]);
        for ($i = 0; $i < count($Toptions); $i++){
            echo "<h3>".$Toptions[$i]."</h3>";
        }
        echo "</td><td>";
        echo "<form action='user.php' method='GET'>";
        echo "    <input type='hidden' name='dispatch' value='set_relation'/>";
        echo "    <input type='hidden' name='set_relation' value='".$_SESSION["TIdR"]."'>";
        echo "    <input type='tag' name='tag' required='required'>";
        echo "    <input type='submit' value='ajouter un tag'>";
        echo "</form>";
        echo "<form action='user.php' method='GET'>";
        echo "    <input type='hidden' name='dispatch' value='mod_relation'/>";
        echo "    <input type='hidden' name='mod_relation' value='".$_SESSION["TIdR"]."'>";
        echo "    <input type='tag'  name='tag' list='tag_input' required='required'>";
        echo "    <input type='submit' value='enlever un tag'>";
        echo "</form>";
        echo "<form action='user.php' method='GET'>";
        echo "    <input type='hidden' name='dispatch' value='del_relation'/>";
        echo "    <input type='hidden' name='del_relation' value='".$_SESSION["TIdR"]."'>";
        echo "    <input type='submit' value='enlever contact'>";
        echo "</form>";
        echo "</td>";
        echo "</tr>";
        unset($_SESSION["TIdR"]);
        unset($_SESSION["Toptions"]);
        };
    echo "</table>";
}

function dispatcher(){
    /// echo "<h3>dispatcher ";
    /// echo var_dump($_GET);
    /// echo var_dump($_SESSION);
    /// echo "</h3>";
    if (isset($_GET["dispatch"])){
    if ($_GET["dispatch"] == "connection") {
        SQLCoServe(function ($conn){Connect_User($conn);});
        return ;
    }
    elseif ($_GET["dispatch"] == "disconnect"){
        Disconnect_user();
        return ;
    }
    elseif ($_GET["dispatch"] == "create") {
        SQLCoServe(
            function ($conn){Creat_user($conn);}
        );
        return;
    }
    if ($_GET["dispatch"] == "home") {
        /// when returning to 'home' just reset the sql querry
        /// could be use to have command history
        $_SESSION["sql"] = "select DISTINCT * from client join relation on client.Idclient=relation.IdCB and relation.IdCA=".$_SESSION["id"];
        unset($_SESSION["oder"]);
        unset($_SESSION["tag"]);
    }
    elseif ($_GET["dispatch"] == "set_relation") {
        SQLCoServe(function ($conn){
            SQLinsert($conn,"UPDATE relation SET TagR = CONCAT(TagR, ';".$_GET["tag"]."') WHERE IdR=".$_GET["set_relation"].";");
        });
        echo "<meta http-equiv='refresh' content='0; url=/user.php'/>";
    }
    elseif ($_GET["dispatch"] == "mod_relation"){
        SQLCoServe(function ($conn){
            $tags = explode(";",SQLselect($conn,"select TagR from relation where IdR=".$_GET["mod_relation"])[0]["TagR"]);
            array_push($tags," ");
            $key = array_search($_GET["tag"], $tags);
            unset($tags[$key]);
            $tag = "";
            for ($i = 0; $i < count($tags); $i++){$tag = $tag . $tags[$i];}
            SQLinsert($conn,"UPDATE relation SET TagR = '".$tag."' WHERE IdR=".$_GET["mod_relation"].";");
        });
        echo "<meta http-equiv='refresh' content='0; url=/user.php'/>";
    }
    elseif ($_GET["dispatch"] == "del_relation") {
        SQLCoServe(function ($conn){
            SQLinsert($conn,"DELETE FROM `relation` WHERE `relation`.`IdR`=".$_GET["del_relation"]);
        });
        echo "<meta http-equiv='refresh' content='0; url=/user.php'/>";
    }
    elseif ($_GET["dispatch"] == "app_order_up"){
        array_push($_SESSION["order_c"],array($_GET["oder"],1));
        echo "<meta http-equiv='refresh' content='0; url=/user.php'/>";
    }elseif ($_GET["dispatch"] == "app_order_down"){
        array_push($_SESSION["order_c"],array($_GET["oder"],2));
        echo "<meta http-equiv='refresh' content='0; url=/user.php'/>";
    }
    elseif ($_GET["dispatch"] == "add_friend"){
        SQLCoServe(function ($conn){
            $max_id = SQLselect($conn,"select count(*) from relation;");
            $max_id = intval($max_id[0]["count(*)"]);
            $max_id = $max_id + 1;
            $b = SQLselect($conn,"select Idclient from client where Cusername='".$_GET["contact"]."'");
            if (count($b)==1){
                $b = intval($b[0]["Idclient"]);
                SQLinsert($conn,"insert into `relation` (IdR,IdCA,IdCB,TagR) values (".$max_id.",".$_SESSION["id"].",".$b.",' ')");
            }
        });
        echo "<meta http-equiv='refresh' content='0; url=/user.php'/>";
    }
    elseif ($_GET["dispatch"] == "tag") {
        $_SESSION["tag"] =  $_GET["tag"];
        echo "<meta http-equiv='refresh' content='0; url=/user.php'/>";
    }
    }
    SQLCoServe(function ($conn){
        $s = "";
        $a = array();
        if (isset($_SESSION["tag"])){
        $a = explode(";",$_SESSION["tag"]);}
        if (count($a) != 0){
        for ($i = 0; $i < count($a); $i++){
            if ($i == 0){
            $s = "relation.TagR like '%".$a[0]."%'";
            }
            else{
                $s = $s . " and relation.TagR like '%".$a[$i]."%'";
            }
        }}
        $sql = $_SESSION["sql"];
        if (isset($_SESSION["tag"])){$sql = $sql . " where " . $s . " ";}
        if (count($_SESSION["order_c"])>0){
            $sql = $sql . " order by ";
            if ($_SESSION["order_c"][0][1] == "2"){ "client.C" . $_SESSION["order_c"][0][0] . " asc";}
            else {$sql = $sql . " client.C" . $_SESSION["order_c"][0][0] . " desc";}
            for ($i = 1; $i < count($_SESSION["order_c"]); $i++){
            if ($_SESSION["order_c"][$i][1] == "2"){ ",client.C" . $_SESSION["order_c"][$i][0] . " asc ";}
            else {$sql = $sql . ",client.C" . $_SESSION["order_c"][$i][0] . " desc ";}
        }}
        echo $sql;
        $board = SQLselect($conn,$sql);
        Get_board($board);
    });
}
?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="images/favicon.ico">
    <link rel="stylesheet" href="style.css">
    <title>motel</title>
</head>

<body>
    <div style="visibility: hidden;">ok</div>
    <div style="visibility: hidden;">ok</div>
    <header>
        <div class="banner">
            <img src="images/logo.png" href="index.html" />
            <h1>montel</h1>
            <details>
                <summary>Mon Compte</summary>
                <form action="user.php" method="GET">
                    <input type="hidden" name="dispatch" value="disconnect">
                    <input type="submit" name="Se Déconnecter" value="Se Déconnecter">
                </form>
                <?php
                if (isset($_SESSION["admin"])&&$_SESSION["admin"]) {
                echo "<button onclick='document.getElementById(\"console_div\").style.display = \"block\";'>console</button>";
                }
                ?>
            </details>
        </div>
    </header>
    <div class="menu">
        <img src="images/home.png" alt="home.png" onclick="document.getElementById('home_form').submit();">
        <form action="user.php" method="GET" id="home_form">
            <input type="hidden" name="dispatch" value="home"/>
            <input type="submit" value="home">
        </form>
        <details>
            <summary>ajouter un contact</summary>
            <form action="user.php" method="GET">
                <input type="text" name="contact" placeholder="username" required="required">
                <input type="submit" name="dispatch" value="add_friend">
            </form>
        </details>
        <details>
            <summary>TAG</summary>
            <form action="user.php" method="GET">
                <input type="text" list="tag_input" name="tag" placeholder="tag">
                <input type="submit" name="dispatch" value="tag">
            </form>
        </details>
    </div>

    <?php
    /// nice to have auto sugest the tags
    echo "<datalist id='tag_input'>";
    if (isset($_SESSION["id"])){
        $options = array();
        SQLCoServe(function ($conn){
            global $options;
            $options = SQLselect($conn,"select TagR from relation where IdCA='".$_SESSION["id"]."'");
        });
        $options = explode(";",$options[0]["TagR"]);
        for ($i = 0; $i < count($options); $i++){
        echo "<option value='".$options[$i]."'>";
    }
    }
    echo "</datalist>";

    /// because i know i want that
    if (isset($_SESSION["admin"])&&$_SESSION["admin"]) {

        if (isset($_GET["dispatch"])&& $_GET["dispatch"] == "commande"){
            echo "<style type='text/css'>#console_div {display: block !important;}</style>";
            echo "<h3>command visible</h3>";
        };

        echo "<div id='console_div'>";
        echo "    <h3>php console</h3>";
        echo "    <form action='user.php' method='GET'>";
        echo "        <input type='hidden' name='dispatch' value='commande'>";
        echo "        <input type='text' name='eval' value=\"echo 'hello';\">";
        echo "        <input type='submit' name='Submit' value='Submit'>";
        echo "    </form>\n";
        
        if (array_key_exists("eval",$_GET)) {
            echo "<h3>command was</h3><h3>";
            echo $_GET["eval"];
            echo "</h3><h3>result is </h3><h3>";
            echo(eval($_GET["eval"]));
            echo "</h3>";
        }
        
        echo "<h3>js console</h3>";
        echo "<textarea id='js_console' cols='30' rows='5'>alert(\"hi\");</textarea>";
        echo "<button onclick='document.getElementById(\"result_js\").innerText = eval(document.getElementById(\"js_console\").value);'>eval js</button>";
        echo "<h3>js return</h3>";
        echo "<h3 id='result_js'></h3>";
        echo "</div>\n";
        echo "<h3>";
        echo "</h3>";
    }
    
    dispatcher();
    ?>

    <footer>
        <div class="center">
            <h3>Ce site utilise des cookies</h3>
            <h3>prototype de gestion de numéro de téléphone</h3>
            <h3>Crédit : PAVARD Arthur JEAN-LOUIS Florian</h3>
            <h3><?php echo 'Version PHP courante : ' . phpversion(); ?></h3>
            <h3>Motel.inc tous droits réserver</h3>
        </div>
    </footer>
    <div style="visibility: hidden;">ok</div>
    <div style="visibility: hidden;">ok</div>
</body>

</html>