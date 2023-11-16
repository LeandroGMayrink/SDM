function calcularIdade() {
      const anoNascimento = document.getElementById('anoNascimento').value;
      const anoAtual = document.getElementById('anoAtual').value;

      const idadeAgora = anoAtual - anoNascimento;
      const idadeEm2050 = 2050 - anoNascimento;

      const resultadoElement = document.getElementById('resultado');
      resultadoElement.innerHTML = `<p>Idade no ano atual: ${idadeAgora} anos</p><p>Idade em 2050: ${idadeEm2050} anos</p>`;
      resultadoElement.classList.add('resultado-background');
    }