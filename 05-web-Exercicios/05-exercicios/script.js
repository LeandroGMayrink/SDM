 function calcularHipotenusa() {
      var catetoA = parseFloat(document.getElementById('catetoA').value);
      var catetoB = parseFloat(document.getElementById('catetoB').value);

      if (isNaN(catetoA) || isNaN(catetoB)) {
        alert('Por favor, insira valores válidos para os catetos.');
        return;
      }

      var hipotenusa = Math.sqrt(Math.pow(catetoA, 2) + Math.pow(catetoB, 2));

      const resultadoElement = document.getElementById('resultado');
      resultadoElement.innerHTML = `<p class="text-white">A hipotenusa é:   ${hipotenusa.toFixed(2)}</p>`;
      resultadoElement.classList.add('resultado-background');
    }
