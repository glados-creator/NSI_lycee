// Référencement par des variables Javascript des éléments HTML à manipuler:
let cercleAntiCSS = document.getElementById('cercleAntiCSS');

// Gestion de la disparition des règles CSS:
function disparitionCSS() {
  document.children[0].children[0].children[2].removeAttribute('href');
}

cercleAntiCSS.onclick = disparitionCSS;