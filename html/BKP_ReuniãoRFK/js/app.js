// Função para exibir um alerta na página quando ela é recarregada
function alerta() {
  alert('Cancelamentos de reunião com a ANA DA RECEPÇÃO ou em seu e-mail, caso tenha alguma dúvida, FAVOR verificar o RODAPÉ da página');
}
// Obtem elementos de hora, minuto e segundo do relógio
const horas = document.getElementById('horas');
const minutos = document.getElementById('minutos');
const segundos = document.getElementById('segundos');

// Função para atualizar o relógio
function atualizarRelógio() {
  const dateToday = new Date();
  let hr = dateToday.getHours();
  let min = dateToday.getMinutes();
  let s = dateToday.getSeconds();

  // Formata as horas, minutos para adicionar um zero à esquerda se necessário
  if (hr < 10) hr = '0' + hr;
  if (min < 10) min = '0' + min;
  if (s < 10) s = '0' + s;

  // Atualiza os elementos de horas, minutos e segundos com os valores formatados
  horas.textContent = hr;
  minutos.textContent = min;
  segundos.textContent = s;
}
// Função para obter a localização do usuáro e atualizar ou mostrar um alerta
function obterLocalizacaoEAtualizarRelógio() {
  if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(function (position) {
          const latitude = position.coords.latitude;
          const longitude = position.coords.longitude;

          // Coordenadas geográficas do estado do Paraná
          const latitudeParana = -25.252088;
          const longitudeParana = -52.021499;

          // Margem de erro para a correspondência
          const margemErro = 0.5; // Exemplo de margem de erro

          // Verifica se as coordenadas do usuário correspondem ao Paran
          if (
              Math.abs(latitude - latitudeParana) <= margemErro &&
              Math.abs(longitude - longitudeParana) <= margemErro
          ) {
              // Exibe o alerta apenas para usuários no Paraná
              alerta();
          } else {
              // Atualiza o relógio com a hora local
              atualizarRelógio();
          }
      });
  } else {
      // Navegador não suporta geolocalização
      atualizarRelógio();
  }
}

// Chama a função para obter a localização do usuário e atualizar o relógio
obterLocalizacaoEAtualizarRelógio();

// Atualize o relógio a cada segundo
setInterval(atualizarRelógio, 1000);

// Função da data
function mostrarDataAtualizada() {
  var elementoData = document.getElementById("dataAtual");

  function atualizarData() {
      var dataAtual = new Date();
      var dia = dataAtual.getDate();
      var mes = dataAtual.getMonth() + 1;
      var ano = dataAtual.getFullYear();

      var dataFormatada = dia + '/' + mes + '/' + ano;

      elementoData.innerHTML = dataFormatada;
  }
  // Chama a função para exibir a data atual
  atualizarData();

  // Atualiza a data a cada segundo
  setInterval(atualizarData, 1000);
}
// Chama a função para mostrar a data atualizada
mostrarDataAtualizada();