"use strict";

function normalize(str) { //prend le texte, passe les maj en min, et remplace les é par des e
    return str.toLowerCase().replace('é', 'e');
}

function clicSurItem(event) {
    let sportName = event.currentTarget.textContent;
    let aAjouter = document.createElement("p");
    let aAjouterText = (sportName + ": " + sportsV1[normalize(sportName)] + " licenciés");

    if (!(dejaDedans.includes(normalize(sportName)))) {
        asideInfo.appendChild(aAjouter);
        aAjouter.textContent = aAjouterText;
        dejaDedans.push(normalize(sportName));
    }

    if (dejaDedans.length >= 2) {
        leBouton.style.display = "block";
    }
}

function resetALL(event) {
    console.log("Et pouf, y a plus rien (non)");
    document.documentElement.innerHTML = ':)';
    document.documentElement.style.textAlign = "center";
    document.documentElement.style.fontSize = "450px";
}