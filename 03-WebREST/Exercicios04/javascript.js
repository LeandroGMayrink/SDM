$(document).ready(function () {
  function buscarPerguntas() {
    var apiUrl = "https://opentdb.com/api.php?amount=10&category=11&difficulty=easy&type=multiple";

    $.ajax({
      url: apiUrl,
      method: "GET",
      success: function (data) {
        $("#perguntas").empty();

        data.results.forEach(function (pergunta, index) {
          var perguntaHtml = `
                      <div class="pergunta">
                          <p><strong>Pergunta ${index + 1}:</strong> ${pergunta.question}</p>
                          <ul class="opcoes">
                              ${pergunta.incorrect_answers.map(opcao => `<li>${opcao}</li>`).join("")}
                              <li>${pergunta.correct_answer}</li>
                          </ul>
                      </div>
                  `;
          $("#perguntas").append(perguntaHtml);
        });
      },
      error: function () {
        $("#perguntas").html("<p>Erro ao buscar perguntas.</p>");
      }
    });
  }

  $("#buscarPerguntas").on("click", buscarPerguntas);
});
