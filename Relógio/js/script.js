const horas = document.getElementById('horas');
const minutos = document.getElementById('minutos');
const segundos = document.getElementById('segundos');

const relogio = setInterval(function time() {
    let dateToday = new Date();
    let horaATUAL = dateToday.getHours();
    let minutoATUAL = dateToday.getMinutes();
    let segundoATUAL = dateToday.getSeconds();

    if (horaATUAL < 10) {
        horaATUAL = '0' + horaATUAL;
    }

    if (minutoATUAL < 10) {
        minutoATUAL = '0' + minutoATUAL;
    }
    
    if (segundoATUAL < 10) {
        segundoATUAL = '0' + segundoATUAL;
    }

    horas.textContent = horaATUAL;
    minutos.textContent = minutoATUAL;
    segundos.textContent = segundoATUAL;
})