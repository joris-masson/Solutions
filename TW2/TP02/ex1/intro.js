"use strict";

/********* TABLEAUX **********/

let tableau1 = [2, 5, 9, 45, 1, 5, 7, 9];
let tableau2 = [9, 12, 4, 78, 0, 45, 2, 10, 29];

/********* OBJETS **********/

let objet1 = {
    "title": "le titre",
    "liste": [5, 8, 9]
};

let objet2 = {
    "contact": {
        "email": "toto@gmail.com",
        "phone": "098765432"
    },
    "stores": {
        "sousObjet1": {
            "name":"BestStore",
            "city":"Houston"
        },
        "sousObjet2": {
            "name":"TestZone",
            "city":"Paris"
        },
        "sousObjet3": {
            "name":"ZeStore",
            "city":"London"
        },
    }
};


function sommeTab(tab) {
    let som = 0;
    for (let i = 0; i < tab.length; i++) {
        som += tab[i];
    }
    return som;
}

function lastTab(tab) {
    let last = tab[tab.length - 1];
    return last;
}

function lastElems(tab, n) {
    if (n >= tab.length) {
        return tab;
    } else {
        let last = [];
        for (let i = (tab.length - n); i < tab.length; i++) {
            last.push(tab[i]);
        }
        return last;
    }
}

function elemsSup(tab, n) {
    let sup = [];
    for (let i = 0; i < tab.length; i++) {
        if (tab[i] > n) {
            sup.push(tab[i]);
        }
    }
    return sup;
}

function elemsCommuns(tab1, tab2) {
    let communs = [];
    if (tab1 < tab2) {
        for (let i = 0; i < tab2.length; i++) {
        if (tab1.indexOf(tab2[i]) != -1) {
            communs.push(tab2[i]);
            }
        }   
    } else {
        for (let i = 0; i < tab1.length; i++) {
        if (tab2.indexOf(tab1[i]) != -1) {
            communs.push(tab1[i]);
            }
        }
    }
    
    return communs;
}

function sansCommuns(tab1, tab2) {
    let communs = elemsCommuns(tab1, tab2);
    let sansCommuns = [];
    for (let i = 0; i < tab1.length; i++) {
        if ((communs.indexOf(tab1[i]) == -1) && (sansCommuns.indexOf(tab1[i]) == -1)) {
            sansCommuns.push(tab1[i]);
        }
    }
    for (let i = 0; i < tab2.length; i++) {
        if ((communs.indexOf(tab2[i]) == -1) && (sansCommuns.indexOf(tab2[i]) == -1)) {
            sansCommuns.push(tab2[i]);
        }
    }
    return sansCommuns;
}

//tableaux
console.log(sommeTab(tableau1));
console.log(lastTab(tableau1));
console.log(lastElems(tableau1, 12))
console.log(elemsSup(tableau1, 5))
console.log(elemsCommuns(tableau1, tableau2));
console.log(sansCommuns(tableau1, tableau2));

//objets
console.log(objet1);
console.log(objet2);

//objets, suite
function int2Coord(int1, int2) {
    let point = {
        "x": int1,
        "y": int2
    };
    return point;
}
let A = int2Coord(2,-6);
let B = int2Coord(2,3);
let C = int2Coord(-7,3);

function distance(a, b) {
    return Math.sqrt(Math.pow(b['x']-a['x'],2)+Math.pow(b['y']-a['y'],2));
}

console.log(distance(A, B));
