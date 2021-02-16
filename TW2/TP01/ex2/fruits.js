"use strict";

let fruits = ['banane', 'fraise', 'kumquat', 'litchi', 'durian'];

alert(fruits);
console.log(fruits);

function afficherFruits(tab) {
    for (let i = 0; i < tab.length; i++) {
            console.log('fruit numéro ', i, ': ', tab[i]);
    }
}

afficherFruits(fruits);

let aAjouter = prompt("Donnez un nom de fruit: ");
fruits.push(aAjouter);
afficherFruits(fruits);

function demanderPlusieursFruits(n) {
    let ajout;
    for (let i = 0; i < n; i++) {
        ajout = prompt("Donnez un nom de fruit: ");
        fruits.push(ajout);
    }
}

demanderPlusieursFruits(3);
afficherFruits(fruits);