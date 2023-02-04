<?php
$_POST["dispatch"] = "information";
include "acces.php";
# normal stuff déja dans acces.php
bar_nav();
normal();
?>
<div class="center">

    <table style="border: 1cm; border-radius: 0.11cm;border-color: grey;box-shadow: 0 4px 10px 0 rgb(0 0 0 / 20%), 0 4px 20px 0 rgb(0 0 0 / 19%);border-collapse: collapse;display: table;width: 100%;">
    <thead>
        <tr>
            <th>nom</th>
            <th>prénom</th>
<?php
if (isset($_SESSION["admin"])){
    echo "<th>supprimé</th>
    <th>voir</th>
    <th>changer le mot de passe</th>
    ";
}
?>
        </tr>
</thead>
<tbody id="membertableau">
<tr></tr>
<tbody>
    </table>
    <script>
<?php 
echo("const memberlist = " .json_encode(@echolistmembre(),JSON_HEX_TAG | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_HEX_AMP | JSON_UNESCAPED_UNICODE));
echo (";");
?>
        memberlist.forEach(element => {
            const elem = document.createElement("tr");
            const td1 = document.createElement("td");
            td1.innerText = element["nom"];
            const td2 = document.createElement("td");
            td2.innerText = element["prenom"];
            <?php if(isset($_SESSION["admin"])){?>

            const td3td = document.createElement("td");
            const td3 = document.createElement("form");
            td3td.appendChild(td3);
            td3.style = "display: block !important";
            td3.setAttribute("method", "post");
            td3.setAttribute("action", "admin.php");
            const td3i = document.createElement("input");
            td3i.style = "display: block !important";
            td3i.setAttribute("type", "hidden");
            td3i.setAttribute("name", "admin");
            td3i.setAttribute("value","delete");
            const td3v = document.createElement("input");
            td3v.setAttribute("type", "hidden");
            td3v.setAttribute("name", "delete");
            td3v.setAttribute("value",element["ID"]);
            const td3s = document.createElement("input");
            td3s.setAttribute("type", "submit");
            td3s.setAttribute("value", "supprimer");
            td3.appendChild(td3i);
            td3.appendChild(td3v);
            td3.appendChild(td3s);

            const td4td = document.createElement("td");
            const td4 = document.createElement("form");
            td4td.appendChild(td4);
            td4.style = "display: block !important";
            td4.setAttribute("method", "post");
            td4.setAttribute("action", "admin.php");
            const td4i = document.createElement("input");
            td4i.style = "display: block !important";
            td4i.setAttribute("type", "hidden");
            td4i.setAttribute("name", "admin");
            td4i.setAttribute("value","voir");
            const td4v = document.createElement("input");
            td4v.setAttribute("type", "hidden");
            td4v.setAttribute("name", "voir");
            td4v.setAttribute("value",element["ID"]);
            const td4s = document.createElement("input");
            td4s.setAttribute("type", "submit");
            td4s.setAttribute("value", "voir");
            td4.appendChild(td4i);
            td4.appendChild(td4v);
            td4.appendChild(td4s);

            const td5td = document.createElement("td");
            const td5 = document.createElement("form");
            td5td.appendChild(td5);
            td5.style = "display: block !important";
            td5.setAttribute("method", "post");
            td5.setAttribute("action", "admin.php");
            const td5i = document.createElement("input");
            td5i.style = "display: block !important";
            td5i.setAttribute("type", "hidden");
            td5i.setAttribute("name", "admin");
            td5i.setAttribute("value","pass");
            const td5v = document.createElement("input");
            td5v.setAttribute("type", "hidden");
            td5v.setAttribute("name", "pass");
            td5v.setAttribute("value",element["ID"]);
            const td5s = document.createElement("input");
            td5s.setAttribute("type", "submit");
            td5s.setAttribute("value", "password");
            td5.appendChild(td5i);
            td5.appendChild(td5v);
            td5.appendChild(td5s);

            <?php } ?>
            elem.appendChild(td1);
            elem.appendChild(td2);
            <?php if(isset($_SESSION["admin"])){?>
            elem.appendChild(td3td);
            elem.appendChild(td4td);
            elem.appendChild(td5td);
            <?php } ?>
            document.getElementById("membertableau").appendChild(elem);
        });
    </script>
    <?php space();?>
    <img src="./images/coockie.jpeg" alt="./images/coockie.jpeg">
</div>
<?php
normal_end();
bar_footer();