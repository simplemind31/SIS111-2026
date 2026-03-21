import readline from "node:readline/promises";
import {stdin as input, stdout as output} from "node:process";

const rl=readline.createInterface({input,output});

const a=await rl.question("a: ");
const b=await rl.question("b: ");
const c=await rl.question("c: ");

if(a>=c){
    if(a>=b)console.log(`El numero mayor es ${a}`)
    else console.log(`El numero mayor es ${b}`)
}else{
    if(b>=c)console.log(`El numero mayor es ${b}`)
    else console.log(`El numero mayor es ${c}`)
}   
if(a<=c){
    if(a<=b)console.log(`El numero menor es ${a}`)
    else console.log(`El numero menor es ${b}`)
}else{
    if(b<=c)console.log(`El numero menor es ${b}`)
    else console.log(`El numero menor es ${c}`)
}

rl.close();