"use strict";

function main() {
    let nomSports = getSportName();
    let asideInfo = document.querySelector("#info");

    let listeInfo = document.createElement("ul");

    asideInfo.appendChild(listeInfo);
    for (let i = 0; i < nomSports.length; i++) { //Juste pour tester la f() addItemToList()
        let aAjouter = document.createElement("li");
        aAjouter.textContent = nomSports[i];
        addItemToList(aAjouter, listeInfo);
    }
}

function getSportName() {
    let listeSport = document.querySelector("ol").children; //children pour éviter les blank nodes
    let listeNomSport = [];
    let texte = '';

    for (let i = 0; i < listeSport.length; i++) {
        texte = listeSport[i].textContent;
        listeNomSport.push(listeSport[i].textContent.toLowerCase().replace('é', 'e')); //prend le texte, passe les maj en min, et remplace les é par des e
    }
    console.log(listeNomSport);
    return listeNomSport
}

function addItemToList (item, liste) {
    liste.appendChild(item);
}

console.log("test");