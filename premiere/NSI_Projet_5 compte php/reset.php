<?php
include_once "bar.php";
include_once "acces.php";
bar_header();
bar_nav();
normal();
?>

<div class="center">
    <h3>
        remplacer votre mot de passe <br>
        cette page n'est valable que pendant un jour
    </h3>
    <form action="acces" method="post" class="blockinput center">
    <input type="hidden" name="dispatch" value="password_reset">
    <input type="hidden" name="dispatch_retourn" value="reset.php">
    </form>
</div>

<?php
normal_end();
bar_footer();