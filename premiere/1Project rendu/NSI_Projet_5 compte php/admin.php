<?php

$admin_username = "admin";                      # les admin on acces au system pour le changer
$admin_passwrd = "123456789";

function readdata(){
    $database = json_decode(file_get_contents("database.json"),true);
    #select json result by ID
    $select = $database[$_POST['voir']];
    #creat user from json
    
    echo("ID <br>");
    echo($_POST ['voir']);
    echo(" <br>NOM  <br>") ;
    echo( $select ["NOM"]);
    echo(" <br>PRENOM  <br>") ;
    echo( $select ["PRENOM"]);
    echo(" <br>USERNAME  <br>") ;
    echo($select ["USERNAME"]);
    echo(" <br>DATE_CREATE  <br>") ;
    echo($select ["DATE_CREATE"]);
    echo(" <br>DATE_BIRTH  <br>") ;
    echo( $select ["DATE_BIRTH"]);
    echo(" <br>PHONE  <br>") ;
    echo($select ["PHONE"]);
    echo(" <br>ADDRESS  <br>") ;
    echo($select ["ADDRESS"]);
    echo(" <br>EMAIL  <br>") ;
    echo($select ["EMAIL"]);
}

function password(){
    $database = json_decode(file_get_contents("database.json"),true);
    #select json result by ID

    $rand = random_int(100,1500);
    $database[$_POST['pass']]["password"] = hash("sha256",$rand);
    echo $rand;

    $datafile = fopen("database.json", "w");
    # write
    fwrite($datafile,json_encode($database , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE),strlen(json_encode($database , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE)));
    # close
    fclose($datafile);
}

function delete(){
    # da delete an ID
    # for reason like spam user we don't really delet everything
    # because the ID will be taken forever we will keep the name and date of creating
    $database = json_decode(file_get_contents("database.json"),true);
    $user = null;

    foreach ($database as &$val){
        if ($_POST["delete"] == $val["ID"]){
            $user = &$val;
            break;
        }
    }
    echo var_dump($user);
    #abase[user["ID"]}->{"ID"} = null;
    $user["NOM"] = null;
    #abase[user}->{"PRENOM"} = null;
    $user["USERNAME"] = null;
    $user["password"] = null;
    #abase[use]}->{"DATE_CREATE"} = null;
    $user["DATE_BIRTH"] = null;
    $user["PHONE"] = null;
    $user["ADDRESS"] = null;
    $user["EMAIL"] = null;

    $datafile = fopen("database.json", "w");
    # write
    fwrite($datafile,json_encode($database , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE),strlen(json_encode($database , JSON_PRETTY_PRINT|JSON_UNESCAPED_UNICODE)));
    # close
    fclose($datafile);
    
}

function admin(){
    session_start();
    echo'
    <!doctype html>
    <html>
    <head>
      <meta charset ="utf-8" />
      <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
      <link rel="stylesheet" href="style.css">
      <title> club informatique </title>
    </head>
  
    <body>';

    switch ($_POST["admin"]){
        case "message":
            echo "OK";
        case 'voir':
            readdata();
            die();
        case 'pass':
            password();
            die();
        case "delete":
            delete();
            echo "OK";
            die();
        default:
            $s = "Internal error '{$_POST["admin"]}' unknonw";
            die($s);
    }

}

if (isset($_POST["admin"])){admin();}
