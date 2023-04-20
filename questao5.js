// ## Questão 5

// Escreva um programa que inverta os caracteres de um string.

// IMPORTANTE:
// a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
// b) Evite usar funções prontas, como, por exemplo, reverse;

const inputString = 'Eduardo';
let outputString = '';

for (let i = 0; i < inputString.length; i++) {
  outputString = inputString[i] + outputString;
}

console.log(outputString);
