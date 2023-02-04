<?php
include "bar.php";
bar_header();
bar_nav();
normal();
?>
<!-- s incrire -->
  <fieldset>
    <legend>s'incrire</legend>
    <form action="acces.php" method="POST" class="blockinput center">
      <input type="hidden" name="dispatch" value="inscription">
      <input type="hidden" name="dispatch_retourn" value="login.php">
      nom de famille
      <input type="text" name="name" placeholder="nom de famille">
      prénom
      <input type="text" name="prenom" placeholder="prénom">
      nom d'utilisateur
      <input type="text" name="username" placeholder="nom d'utilisateur">
      mot de passe
      <input type="password" name="password" placeholder="mot de passe">
      confirmer le mot de passe
      <input type="password" name="password1" placeholder="mot de passe">
      <div class="collapsible">
        <div class="center">
          <h3>le mot de passe doit avoir au moins</h3>
          <ul>
            <li>8 caractères</li>
            <li>1 caractère majuscule</li>
            <li>1 caractère minuscule</li>
            <li>1 caractère spécial so possible</li>
          </ul>
        </div>
      </div>
      <div id="password_warning" style="visibility: hidden; display: none;">Vous ne respecter pas les règles <br> pour crée un mot de passe</div>
      numéros de téléphone
      <input type="tel" name="tel" placeholder="numéros de téléphone">
      date de naissance
      <input type="date" name="date_birth" placeholder="date de naissance">
      address
      <input type="text" name="address" placeholder="address">
      address mail
      <input type="email" name="email" placeholder="email">
      <input type="submit" name="incrire" value="s'incrire">
    </form>
  </fieldset>
<?php
normal_end();
bar_footer();