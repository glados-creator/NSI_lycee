<?php
include_once "bar.php";
bar_header();
bar_nav();
normal();
?>

<div class="center">
  <fieldset>
    <legend>se connecter</legend>
    <form action="acces.php" method="POST">
      <input type="hidden" name="dispatch" value="connection">
      <input type="hidden" name="dispatch_retourn" value="connect.php">
      nom d'utilisateur
      <input type="text" name="username" placeholder="nom d'utilisateur">
      mot de passe
      <input type="password" name="password" placeholder="mot de passe">
      <input type="submit" name="se connecter" value="se connecter">
    </form>
  </fieldset>
</div>

<?php
normal_end();
bar_footer();
