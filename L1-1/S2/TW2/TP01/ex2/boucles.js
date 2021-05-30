'use strict';

for (let i = 0; i <= 100; i++) {
    console.log(i);
}

let debut = prompt("Le début: ");
let fin = prompt("La fin: ");

if (fin - debut >= 100000) {
    alert("Vous feriez mieux de recharger la page avant de faire planter votre navigateur :)")
}

for (let i = debut; i <= fin; i++) {
    if (i%3 == 0) {
        console.log(i);
    }
}