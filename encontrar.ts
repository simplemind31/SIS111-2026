import readline from "node:readline/promises";
import {stdin as input, stdout as output} from "node:process";
const rl=readline.createInterface({input,output});
function generar(limite:number){
    let numeroran=new Array();
    for(let i=0;i<limite;i++){
        numeroran.push(Math.random()*100);
    }
    return numeroran;
}
function buscar(limite:number,x:number){
    let a=generar(limite);
    let con=0;
    a.forEach(element => {
        con+=Number(element==x);
    });
    return {
        "mensaje":`El numero de coincidencias de ${x} es ${con}`,
        "resultado":a
    }
}