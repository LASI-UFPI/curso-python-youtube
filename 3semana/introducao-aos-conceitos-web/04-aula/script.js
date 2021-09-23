// Função para clicar
function clicar() {
  console.log("Você clicou");
}

function nome() {
  var nome;
  nome = prompt("Digite o seu nome!");
  alert(`Olá, ${nome}, tudo bem?`);
}

function mudarTexto() {
  var text = document.getElementById("title");

  console.log(text.innerText);

  text.innerText = "Proxima Aula vai ser de Django!";
}
