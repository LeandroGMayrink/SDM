async function gerarDados() {
  const template = document.getElementById('template').value;
  const resultadoDiv = document.getElementById('resultado');

  try {
    const response = await fetch(`https://dummyjson.com/api?template=${encodeURIComponent(template)}`);
    const data = await response.text();
    resultadoDiv.innerHTML = `<pre>${data}</pre>`;
  } catch (error) {
    resultadoDiv.textContent = 'Ocorreu um erro ao gerar os dados.';
  }
}