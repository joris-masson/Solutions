"use strict";

let oeuvre = {
    "auteur": "Jacques-Louis David",
    "titre": "Le Sacre de Napoléon",
    "annee": 1807,
    "hauteur": 621,
    "largeur": 979,
    "url": "https://fr.wikipedia.org/wiki/Le_Sacre_de_Napol%C3%A9on"
};

alert(oeuvre);
console.log(oeuvre);

oeuvre['titre'] = "The Courtyard of the Old Residency in Munich";
console.log(oeuvre);

console.log((oeuvre['hauteur']*oeuvre['largeur'])/10000);

let animal = {
    'nom': 'Nala',
    'espece': 'chien',
    'age': 3
};

console.log(animal);