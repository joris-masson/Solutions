'use strict';

function Far2Cel(temp) {
    return ((temp-32)*5)/9;
}

console.log(Far2Cel(68));

let aConv = prompt("Veuillez entre une température en °F: ");
console.log(Far2Cel(aConv), '°C');