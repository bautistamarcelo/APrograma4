

document.getElementById('btnDetalleAcerca').addEventListener('click', function () {
    if (document.getElementById('btnDetalleAcerca').innerHTML == "MAS DETALLES") {
        document.getElementById('btnDetalleAcerca').innerHTML = "Informado";
        alert('Mostraría información adiscional');
    } else {
        document.getElementById('btnDetalleAcerca').innerHTML = "MAS DETALLES";
    }

});

document.getElementById('btnImprimeCV').addEventListener('click', function () {
    if (document.getElementById('btnImprimeCV').innerHTML == "Imprimir CV") {
        document.getElementById('btnImprimeCV').innerHTML = "Enviado a Impresión";
        alert('Mostraría el CV en PDF para su eventual impresión');
    } else {
        document.getElementById('btnImprimeCV').innerHTML = "Imprimir CV";
    }

});

document.getElementById('btnSaberMas').addEventListener('click', function () {
    if (document.getElementById('btnSaberMas').innerHTML == "Saber Más") {
        document.getElementById('btnSaberMas').innerHTML = "INFORMADO";
        alert('Mensaje adiscional con información complementaria, podría ser de una sección oculta o un pdf');
    } else {
        document.getElementById('btnSaberMas').innerHTML = "Saber Más";
    }

});

document.getElementById('btnReferencias').addEventListener('click', function () {
    if (document.getElementById('btnReferencias').innerHTML == "Obtener Referencias") {
        document.getElementById('btnReferencias').innerHTML = "OBTENIDAS";
        alert('Mensaje adiscional con información complementaria, podría ser de una sección oculta o un pdf');
    } else {
        document.getElementById('btnReferencias').innerHTML = "Obtener Referencias";
    }

});
