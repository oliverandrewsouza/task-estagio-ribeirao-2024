function verificarLetraA(str) {

    const strLowerCase = str.toLowerCase();
    const ocorrencias = (strLowerCase.match(/a/g) || []).length;
    const existeLetraA = ocorrencias > 0;
    
    if (existeLetraA) {
        console.log(`A letra 'a' ocorre ${ocorrencias} vez(es) na string.`);
    } else {
        console.log("A letra 'a' não ocorre na string.");
    }
}

function main() {
    let str = prompt("Digite uma string para verificar a existência e a quantidade da letra 'a':");
    verificarLetraA(str);
}

main();