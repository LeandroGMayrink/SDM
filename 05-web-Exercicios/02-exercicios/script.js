 function calcularNovoSalario() {
      const salarioAtual = parseFloat(document.getElementById('salarioAtual').value);
      if (isNaN(salarioAtual)) {
        alert('Por favor, insira um valor válido para o salário.');
        return;
      }

      const aumentoPercentual = 25;
      const aumentoDecimal = aumentoPercentual / 100;
      const novoSalario = salarioAtual * (1 + aumentoDecimal);

      const resultadoElement = document.getElementById('resultado');
      resultadoElement.innerHTML = `<p>O novo salário com aumento de ${aumentoPercentual}% é: <br><br>R$ ${novoSalario.toFixed(2)}</p>`;
      resultadoElement.classList.add('resultado-background');
    }