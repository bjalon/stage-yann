var a = 12
var b = 13
document.getElementById("a").innerHTML = a
document.getElementById("b").innerHTML = b
var resultatSaisi = null

var successfulAudio = new Audio('audio/win.wav');
var failedAudio = new Audio('audio/fail.wav');

function verifierResultatAddition() {
    resultatSaisi = parseInt(document.getElementById("inputResultAddition").value)
    var resultatAttendu = a + b
    var isCorrect = (resultatAttendu === resultatSaisi)
    if (isCorrect) {
        // alert("Le résultat saisi est bon")
document.getElementById("informationAddition").innerHTML = "Le résultat est correct"
document.getElementById("informationAddition").setAttribute("style", "color: lightgreen")
successfulAudio.play();
    } else {
        document.getElementById("informationAddition").innerHTML = "Le résultat est faux"
        document.getElementById("informationAddition").setAttribute("style", "color: red")
        failedAudio.play();
        // alert("Le résultat saisi est faux")
    }

}

function verifierResultatMultiplication() {
    resultatSaisi = parseInt(document.getElementById("inputResultMultiplication").value)
    var resultatAttendu = a * b
    var isCorrect = resultatAttendu === resultatSaisi
    if (isCorrect) {
        document.getElementById("informationMultiplication").innerHTML = "Tu es un génie !"
        document.getElementById("informationMultiplication").setAttribute("style", "color: lightgreen")
        successfulAudio.play();
    } else {
        document.getElementById("informationMultiplication").innerHTML = "Tu t'es trompé ☻"
        document.getElementById("informationMultiplication").setAttribute("style", "color: red")
        failedAudio.play();
    }

}