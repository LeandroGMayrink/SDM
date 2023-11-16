function converterTemperatura() {
  const temperaturaCelsius = parseFloat(document.getElementById('temperaturaCelsius').value);
  if (isNaN(temperaturaCelsius)) {
    alert('Por favor, insira um valor válido para a temperatura em Celsius.');
    return;
  }

  const temperaturaFahrenheit = (temperaturaCelsius * 1.8) + 32;

  const resultadoElement = document.getElementById('resultado');
  resultadoElement.innerHTML = `<p class="text-white">A temperatura em Fahrenheit é:<br><br> ${temperaturaFahrenheit.toFixed(2)}°F</p>`;
  resultadoElement.classList.add('resultado-background');
}