function calcularEsfera() {
      var raio = parseFloat(document.getElementById('raio').value);

      if (isNaN(raio) || raio <= 0) {
        alert('Por favor, insira um valor válido para o raio.');
        return;
      }

      var comprimento = 2 * Math.PI * raio;
      var area = Math.PI * Math.pow(raio, 2);
      var volume = (3 / 4) * Math.PI * Math.pow(raio, 3);

      const resultadoElement = document.getElementById('resultado')
      resultadoElement.innerHTML = `
        Comprimento da esfera: ${comprimento.toFixed(2)} <br>
        Área da esfera: ${area.toFixed(2)} <br>
        Volume da esfera: ${volume.toFixed(2)}
      `;
      resultadoElement.classList.add('resultado-background');
    }
