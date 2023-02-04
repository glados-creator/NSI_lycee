// Référencement par des variables Javascript des éléments HTML à manipuler:
let imgAtome = document.getElementById('atome'),
    disparition = document.getElementById('disparition'),
    choixColor = document.getElementById('choixColor'),
    changeColor = document.getElementById('changeColor');


// Définition des fonctions gérant les actions lors des évènements:
function disparitionAtome() {
  imgAtome.hidden = !(imgAtome.hidden);
  if (imgAtome.hidden) {
    disparition.innerHTML = 'Tout n\'est pas perdu';
  } else {
    disparition.innerHTML = 'Une tragédie atomique';
  }
}

function changementCouleur() {
  document.body.style.color = choixColor.value;
}


// Association des évènements avec les fonctions gérant les actions:
disparition.onclick = disparitionAtome;
changeColor.onclick = changementCouleur;

