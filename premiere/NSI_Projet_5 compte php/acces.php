<?php

use function PHPSTORM_META\type;

include "admin.php";
include "bar.php";

bar_header();

#open database json user file
$database = json_decode(file_get_contents("database.json"),true);

function read_latest_id(){
    # we count the numbers of entry in the database.json
    global $database;
    return count(array_keys($database));
}


function login(){
    global $database;

    $_SESSION["ID"] =            read_latest_id();
    $_SESSION["NOM"] =           $_POST["name"] or ret();
    $_SESSION["PRENOM"] =        $_POST["prenom"] or ret();
    $_SESSION["USERNAME"] =      $_POST["username"] or ret();
    $_SESSION["DATE_CREATE"] =   time();
    $_SESSION["DATE_BIRTH"] =    $_POST["date_birth"] or ret();
    $_SESSION["PHONE"] =         $_POST["tel"] or ret();
    $_SESSION["ADDRESS"] =       $_POST["address"] or ret();
    $_SESSION["EMAIL"] =         $_POST["email"] or ret();

    #verify that all parameter all really correct
    if($_POST['date_birth'] < 1996)
   {
      die("trop jeune");
   }
    $alpha = array("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z");
    $Balpha = array("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
    $num = array("1","2","3","4","5","6","7","8","9");
    $alphabool = false;
    $Balphabool = false;
    $numbool = false;

    foreach ($database as $val){
        if ($val["USERNAME"] == $_POST["username"]){
            die("déja pris");
        }
    }
    $temp = $_POST["password"] or die("pas de mot de pass");
    if (strlen($temp) < 8){die("mot de passe trop court");}              # mot de passe de 8 caractères
    if ($temp != $_POST["password1"]){die("mot de passe différent");}   # confirmer le mot de passe et mot de passse entrer doit être le meme

    foreach ($alpha as $letter){
        if (strpos($temp , $letter !== false) ){
            $alphabool = true;                      # vérifie que il y a au moin une lettre
        }
    }
    foreach ($Balpha as $letter){
        if (strpos($temp , $letter !== false) ){
            $Balphabool = true;                     # vérifie qie il y a ou moin une lettre majuscule
        }
    }
    foreach ($num as $letter){
        if (strpos($temp , $letter !== false) ){
            $numbool = true;                        # vérifie que il y a au moin un chiffre
        }
    }
    if ($Balphabool or $alphabool or $numbool){die("mot de passe non conforme");}

    # push new user on the database
    global $database;
    array_push($database ,array(
        "ID" => $_SESSION["ID"], 
        "NOM" => $_SESSION["NOM"], 
        "PRENOM" => $_SESSION["PRENOM"], 
        "password" => hash("sha256",$temp),
        "USERNAME" => $_SESSION["USERNAME"], 
        "DATE_CREATE" => $_SESSION["DATE_CREATE"], 
        "DATE_BIRTH" => $_SESSION["DATE_BIRTH"], 
        "PHONE" => $_SESSION["PHONE"], 
        "ADDRESS" => $_SESSION["ADDRESS"], 
        "EMAIL" => $_SESSION["EMAIL"]
    ));

    $datafile = fopen("database.json", "w");
    # write
    fwrite($datafile,json_encode($database , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE),strlen(json_encode($database , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE)));
    # close
    fclose($datafile);

    connection();

    ret("accueil.php");
}

function connection(){
    global $admin_passwrd , $admin_username ,$database,$_SESSION;
    # connecte un utilisateur
    if ($_POST["username"] == $admin_username && $_POST["password"] == $admin_passwrd){
        $_SESSION["admin"] = 1;

        $_SESSION["ID"] = 0;
        $_SESSION["NOM"] = "adminnom";
        $_SESSION["PRENOM"] = "adminprenom";
        $_SESSION["USERNAME"] = "adminusername";
        $_SESSION["DATE_CREATE"] = 0;
        $_SESSION["DATE_BIRTH"] = "adminbirthday";
        $_SESSION["PHONE"] = "adminphone";
        $_SESSION["ADDRESS"] = "adminadresse";
        $_SESSION["EMAIL"] = "adminmail";

        ret("accueil.php");
    } else {
        $temp = hash("sha256",$_POST["password"]);
        foreach ($database as &$user){
            if ($_POST["username"] == $user["USERNAME"] and $temp == $user["password"]){
                $_SESSION["ID"] = $user["ID"];
                $_SESSION["NOM"] = $user["NOM"];
                $_SESSION["PRENOM"] = $user["PRENOM"];
                $_SESSION["USERNAME"] = $user["USERNAME"];
                $_SESSION["DATE_CREATE"] = $user["DATE_CREATE"];
                $_SESSION["DATE_BIRTH"] = $user["DATE_BIRTH"];
                $_SESSION["PHONE"] = $user["PHONE"];
                $_SESSION["ADDRESS"] = $user["ADDRESS"];
                $_SESSION["EMAIL"] = $user["EMAIL"];
                # retour a l'accueil
                ret("accueil.php");
            }
        }
        ret();
        return;
    }
}

function send_email(){
    # function to send an email to reset the password
    # of an ID
    die("email reset not implemnted");
}

function echolistmembre(){
    global $database;
    $build = array();
    foreach ($database as $val){
        array_push($build, array(
            "nom" => $val["NOM"],
            "prenom" => $val["PRENOM"],
            "ID" => $val["ID"]
        ));
    };
    return $build;
}

function ret($par = ""){
    global $database;
    # after done rewrite the database so open
    $datafile = fopen("database.json", "w");
    # write
    fwrite($datafile,json_encode($database , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE),strlen(json_encode($database , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE)));
    # close
    fclose($datafile);
    $return = null;
    if (boolval($par)){
        $return = $par;
    }
    elseif(isset($_POST["dispatch_retourn"])){
        $return = $_POST["dispatch_retourn"];
    } else {
        $return = "accueil.php";
    }
    header("Location: " . $return);
    exit();
}

if (!isset($_POST["dispatch"])){
    die("comment tu est arrivé la ?");
}

switch ($_POST["dispatch"]){
    case "inscription":
        login();
        ret();
        break;
    case "connection":
        connection();
        ret();
        break;
    case "information":
        break;
    case "disconnect":
        session_destroy();
        ret("accueil.php");
    case "change_user_name":
        global $database;
        foreach ($database as &$val){
            if ($val["username"] == $_POST["newusername"]){
                die("déja pris");
            }
        }
        unset($val);
        $database[$_SESSION["ID"]]["USERNAME"] = $_POST["newusername"];
        session_destroy();
        ret("accueil.php");
    case "change_email":
        $database[$_SESSION["ID"]]["email"] = $_POST["newmail"];
        session_destroy();
        ret("accueil.php");
    default:
        $s = "Internal error '{$_POST["dispatch"]}' unknonw";
        die($s);
}