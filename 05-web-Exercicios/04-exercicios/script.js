function calcularMedia() {
  const nota1 = parseFloat(document.getElementById('nota1').value);
  const nota2 = parseFloat(document.getElementById('nota2').value);
  const nota3 = parseFloat(document.getElementById('nota3').value);

  if (isNaN(nota1) || isNaN(nota2) || isNaN(nota3)) {
    alert('Por favor, insira valores válidos para as notas.');
    return;
  }

  const media = (nota1 + nota2 + nota3) / 3;

  const resultadoElement = document.getElementById('resultado');
  resultadoElement.innerHTML = `<p class="text-white">A média aritmética é: ${media.toFixed(2)}</p>`;
  resultadoElement.classList.add('resultado-background');
}
