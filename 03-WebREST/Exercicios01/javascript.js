async function getPostagem(id) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
  const json = await response.json();
  mostrarResposta(json, 'respjsonLer');
}

async function getPostagens() {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts');
  const json = await response.json();
  mostrarResposta(json, 'respjsonListar');
}

async function postPostagens() {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
    body: JSON.stringify({
      title: 'Nova Postagem',
      body: 'Essa é a minha mais nova postagem! :D',
      userId: 1,
    }),
  });
  const json = await response.json();
  mostrarResposta(json, 'respjsonCriar');
}

async function atualizarPostagens() {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
    method: 'PUT',
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
    body: JSON.stringify({
      id: 1,
      title: 'Minha Mais Nova Postagem',
      body: 'Essa é a atualização da minha mais nova postagem! :D',
      userId: 1,
    }),
  });
  const json = await response.json();
  mostrarResposta(json, 'respjsonAtualizar');
}

async function modificarPostagens(id) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
    method: 'PATCH',
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
    body: JSON.stringify({
      title: 'Essa é a modificação da minha mais nova postagem! :D',
    }),
  });
  const json = await response.json();
  mostrarResposta(json, 'respjsonModificar');
}

async function removerPostagem(id) {
  await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
    method: 'DELETE',
  });
  mostrarMensagem('Postagem removida com sucesso.', 'respjsonRemover');
}

async function filtrarPostagens(userId) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/posts?userId=${userId}`);
  const json = await response.json();
  mostrarResposta(json, 'respjsonFiltrar');
}

function mostrarResposta(objeto, elementoId) {
  const mensagem = JSON.stringify(objeto, null, 2);
  document.getElementById(elementoId).innerHTML = `<pre>${mensagem}</pre>`;
}

function mostrarMensagem(mensagem, elementoId) {
  document.getElementById(elementoId).textContent = mensagem;
}