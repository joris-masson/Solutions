"use strict";

function testerDom ()
{
    //écrire votre code dans cette fonction
    
    //Question 1
    console.log("-----Question 1-----");
    let para = document.getElementById("paragraphe");
    para.style.color = "red";
    console.log(para);
    console.log(para.tagName);
    
    console.log(para.childNodes);
    console.log(para.children);
    
    //Question 2
    console.log("-----Question 2-----");
    console.log("---a---");
    let li = document.querySelectorAll("li");
    console.log(li.length);
    
    console.log("---b---");
    let liul = document.querySelectorAll("ul > li");
    console.log(liul.length);
    
    console.log("---c---");
    let liste1 = document.getElementById("liste1");
    let liste2 = document.getElementById("liste2");
    console.log("liste1:", (liste1.childNodes).length);
    console.log("liste2:", (liste2.childNodes).length);
    
    console.log("---d---");
    console.log("liste1:", (liste1.children).length);
    console.log("liste2:", (liste2.children).length);
    
    console.log("---e---");
    
    //Question 3
    console.log("-----Question 3-----");
    let legende = document.querySelector("figcaption");
    console.log(legende);
    legende.style.color = "red";
    
    //Question 4
    console.log("-----Question 4-----");
    let listeP = document.querySelectorAll("p");
    console.log(listeP);
    let leP = listeP[(listeP.length - 1)];
    console.log(leP);
    leP.style.fontSize = "30px";
    leP.style.width = "800px";
    
    //Question 5
    console.log("-----Question 5-----");
    let image = document.querySelector("img");
    console.log("---a---");
    console.log(image.getAttribute("alt"));
    console.log(image.alt);
    
    console.log("---b---");
    console.log(image.attributes);
    
    console.log("---c---");
    console.log("Est-ce que l'attribut title est présent:", image.hasAttribute("title"));
    
    console.log("---d---");
    image.setAttribute("src", "https://ensweb.users.info.unicaen.fr/images/premiere_souris_1968.jpg");
    
    console.log("---e---");
    image.removeAttribute("width");
    
    //Question 6
    console.log("-----Question 6-----");
    console.log((document.getElementsByClassName("elt-test").length));
    
    //Question 7
    console.log("-----Question 7-----");
    let liQ7 = document.querySelectorAll(".laclasse.elt-test");
    console.log(liQ7);
    for(let i = 0; i < liQ7.length; i++) {
        liQ7[i].classList.remove("laclasse");
    }
    
    //Question 8
    console.log("-----Question 8-----");
    console.log(legende);
    legende.innerHTML = "177013";
    
}
