"use strict";

function creationDom ()
{
    // fonction à compléter
    let listeEx1 = document.querySelector("#liste");
    console.log(listeEx1);
    listeEx1.removeChild(listeEx1.lastElementChild);
    
    let listeUlEx1 = document.querySelector("ul");
    console.log(listeUlEx1);
    let aAjouterEx1 = document.createElement("li");
    aAjouterEx1.textContent = "J'aime la vie";
    listeUlEx1.appendChild(aAjouterEx1);
    
    let bodyEx1 = document.querySelector("body");
    let h1Ex1 = document.createElement("h1");
    h1Ex1.textContent = "177013";
    bodyEx1.insertBefore(h1Ex1, bodyEx1.firstChild);
    
    let figureEx1 = document.querySelector("figure");
    let pEx1 = document.createElement("p");
    pEx1.textContent = "La raclette, plat originaire du canton du Valais en Suisse, est obtenue en raclant du fromage fondu en surface par la proximité d'une source de chaleur qui peut être un four spécifique, des braises, ou simplement le feu de bois, bien que cette technique soit plus délicate de par la position couchée du fromage, qui, en fondant, aura tendance à couler et s'étaler (Source: https://fr.wikipedia.org/wiki/Raclette)"
    figureEx1.parentNode.insertBefore(pEx1, figureEx1);
    
    let listeLiEx1 = document.querySelectorAll("ul>li");
    for (let i = 0; i < listeLiEx1.length; i++) {
        listeLiEx1[i].style.backgroundColor = "yellow";
    }
}
