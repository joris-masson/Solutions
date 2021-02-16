'use strict';

let listeAnnees = [2008, 2012, 2020, 1800, 1900, 2100, 2000]

function estBissextile(annee) {
    if ((annee%4 == 0) && ((annee%100 !=0) || (annee%400 == 0))) {
        return true;
    } else {
        return false;
    }
}

console.log(estBissextile(1800));

function recupererBissextiles(liste) {
    let newTab = [];
    for (let i = 0; i < liste.length; i++) {
        if (estBissextile(liste[i])) {
            newTab.push(liste[i]);
        }
    }
    return newTab;
}

console.log(recupererBissextiles(listeAnnees));

function plusPetiteBissext(annee) {
    let listeBissex = recupererBissextiles(listeAnnees);
    let min = listeBissex[0];
    for (let i = 0; i < listeBissex.length; i++) {
        if (listeBissex[i] < min) {
            min = listeBissex[i];
        }
    }
    return min;
}

console.log(plusPetiteBissext(listeAnnees));
