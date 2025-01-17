//Detta är en kommentar

/*
Detta är en kommentar 
på flera rader
*/

//console.log används för att skriva ut text, jämför med print i Python
console.log("hej världen!")

//tilldelning av ett värde till variabler
let x = 10; //let betyder att varibaeln kan ändras senare i programmet
const y = 20; //const betyder att vi inte ska ändra på världet
x = x + 1;
console.log(x);
//y = y + 1; //vi kan inte ändra värdet på en konstant!
let mystring = "detta är en textsträng"
console.log(mystring);

//if else: observera (1) parantes  kring logiska uttrycket och (2) måsvingarna
if (x < 11) {
    console.log("X är mindre än 11")
} else {
    console.log)("X är inte mindre än 11")
}

//arrays: syntaxen liknar Python
let myArray = ["a", 2, 3.14, true];
console.log(myArray[2]); //3.14

//for-loop: observra syntax, i detta fall har vi en variabel "i" som börjar på noll, ökar med ett för varje gång loopen körs och kör loopen så länge som i är mindre än 10 och en ökar den med 1 varje gång
for (let i = 0; i < 10; i++) {
    console(i); //skriver ut alla tal från och med 0 till och med 9
}
//ett annat exempel som skriver ut alla heltal från och med 1 till och med 5
for (let i = 1; i < 6; i++) {
    console(i);
}

//obejkt: detta kan vi ta upp igen senare
let myCar = { regNr: "ABC12D", maxFart: 120};
console.log(myCar.regNr);
console.log(myCar.maxFart);
let enAnnanBil = {regNr: "XYZ"}