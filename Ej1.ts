import readline from "node:readline/promises";
import {stdin as input, stdout as output} from "node:process";

const rl=readline.createInterface({input,output});

let a=Number(await rl.question(""));
let b=Number(await rl.question(""));
let c=Number(await rl.question(""));
let menor=a;
let mayor=a;
if(b>mayor)mayor=b;
if(b<menor)menor=b;
if(c>mayor)mayor=c;
if(c<menor)menor=c;

rl.close();
console.log(`Menor: ${menor} Mayor: ${mayor}`);
