async function consultarCEP() {
  const cep = document.getElementById('cep').value.replace(/\D/g, '');
  const resultadoDiv = document.getElementById('resultado');

  if (cep.length !== 8) {
    resultadoDiv.innerHTML = 'CEP deve conter 8 dígitos.';
    return;
  }

  try {
    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const data = await response.json();

    if (data.erro) {
      resultadoDiv.innerHTML = 'CEP não encontrado.';
    } else {
      resultadoDiv.innerHTML = `
              <p>CEP: ${data.cep}</p>
              <p>Logradouro: ${data.logradouro}</p>
              <p>Bairro: ${data.bairro}</p>
              <p>Cidade: ${data.localidade}</p>
              <p>Estado: ${data.uf}</p>
          `;
    }
  } catch (error) {
    resultadoDiv.innerHTML = 'Ocorreu um erro ao consultar o CEP.';
  }
}
