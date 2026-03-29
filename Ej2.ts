import readline from "node:readline/promises";
import {stdin as input, stdout as output} from "node:process";

const rl=readline.createInterface({input,output});
function aleatorios(n:number){
    let pares="",impares=""
    for(let i=0;i<n;i++){
        let numero=Math.ceil(Math.random()*100)
        if(numero%2==0)pares=`${pares} ${numero},`
        else impares=`${impares} ${numero},`
    }
    return `Pares ${pares}\nImpares ${impares}`
}
let n=Number(await rl.question(""));
console.log(aleatorios(n));
rl.close()