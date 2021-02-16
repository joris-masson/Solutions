"use strict"

function afficherNotes() {
    console.log("notes: " ,document.getElementById("notes"));
    
    let notes = document.querySelectorAll(".note");
    let leBody = document.querySelector("body");
    let listeNotes = document.createElement("ol");
    let listeSpan = document.querySelectorAll("span");
    //let parentSpan = document.querySelector("span").parentElement;
    
    leBody.appendChild(listeNotes);
    
    for (let i = 0; i < notes.length; i++) {
        notes[i].style.display = "none";
        listeNotes.appendChild(document.createElement("li"));
        listeNotes.childNodes[i].textContent = notes[i].textContent;
        //parentSpan.replaceChild(document.createElement("p"), listeSpan[i]);
        
    }
    
}
