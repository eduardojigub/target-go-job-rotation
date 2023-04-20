// ## Job Rotation - Target Intern.

// Código realizado para a vaga de estagiário da empresa Target Sistemas.

// ## Questão 2

// Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

// IMPORTANTE:
// Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

function fibonacci(num) {
  let a = 0;
  let b = 1;
  // enquanto B for menor que o numero informado..:
  while (b < num) {
    let temp = b;
    b = a + b;
    a = temp;
  }

  if (b === num) {
    console.log(`${num} pertence à sequência de Fibonacci`);
  } else {
    console.log(`${num} não pertence à sequência de Fibonacci`);
  }
}

// Exemplo de uso da função
fibonacci(21); // retorna "21 pertence à sequência de Fibonacci"
fibonacci(22); // retorna "22 não pertence à sequência de Fibonacci"
