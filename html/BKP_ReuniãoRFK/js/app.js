// // Cria um alerta quando a página é gerada
// function alerta() {
//     alert('Cancelamentos de reunião com a Ana DA RECEPÇÃO ou em seu e-mail, caso tenha alguma duvida FAVOR verificar o RODAPÉ da página')
// }

const horas = document.getElementById('horas');
const minutos = document.getElementById('minutos');
const segundos = document.getElementById('segundos');

const relogio = setInterval(function time(){
    let dateToday = new Date();
    let hr = dateToday.getHours();
    let min = dateToday.getMinutes();
    let s = dateToday.getSeconds();

    if (hr < 10) hr = '0' + hr;

    if (min < 10) min = '0' + min;
    if (s < 10) s = '0' + s;

    horas.textContent = hr;
    minutos.textContent = min;
    segundos.textContent = s;
 })

//Cria um objeto Date com a data e hora atuais
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

    // Chama a função inicialmente para exibir a data atual
    atualizarData();

    // Atualiza a data a cada segundo (1000 milissegundos)
    setInterval(atualizarData, 1000);
  }
  mostrarDataAtualizada();