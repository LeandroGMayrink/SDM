function verificarParImpar() {
  // Obtenha o valor do input
  const numero = document.getElementById("numero").value;

  // Verifique se o número é par ou ímpar
  if (numero % 2 === 0) {
    document.getElementById("resultado").textContent = `${numero} é um número PAR.`;
  } else {
    document.getElementById("resultado").textContent = `${numero} é um número ÍMPAR.`;
  }
}
