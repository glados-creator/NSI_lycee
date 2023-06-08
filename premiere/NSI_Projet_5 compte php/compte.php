<?php
include "bar.php";
bar_header();
bar_nav();
normal();
?>
<form action="acces.php" method="post">
  <input type="hidden" name="dispatch" value="disconnect">
  <input type="hidden" name="dispatch_retourn" value="compte.php">
  <input type="submit" class=".bouttonuser" value="se déconnecter">
</form>
<form action="acces.php" method="post">
  <input type="hidden" name="dispatch" value="change_user_name">
  <input type="hidden" name="dispatch_retourn" value="compte.php">
  <input type="text" name="newusername" placeholder="newusername">
  <input type="submit" class=".bouttonuser" value="changer de nom d'utilisateur">
</form>
<form action="acces.php" method="post">
  <input type="hidden" name="dispatch" value="change_email">
  <input type="hidden" name="dispatch_retourn" value="compte.php">
  <input type="email" name="newmail" placeholder="email">
  <input type="submit" class=".bouttonuser" value="se changer d'addresse mail">
</form>
<?php
normal_end();
bar_footer();
