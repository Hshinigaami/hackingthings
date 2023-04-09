var x = 25;
var x = 30;
// Var variable declaration keyword, we can redclare it multiple times

// let won't redeclare
let y = 30;
// const cannot be updated not even redeclare
const z = 50;

console.log(x,y,z);

// You know most operations we use during mathematical operations some
// of them are === !== 
// first is identical means value and datatype should be same
// second opposite of first

// CONDITIONALS
if(x == 25){
    console.log("Ola");
}else if(y == 25){
    console.log("GOla");
}else {
    console.log("Dola");
};

switch(z){
    case 25:
        console.log("Hat");
        break;
    case 35:
        console.log("Dat");
        break;
    default:
        console.log("Hayla");
};

// FUNCTIONS
// es6 based
const xd = (a,b) => {
    console.log(a, b);
}
xd(20,30)

// OBJECTS AND ARRAYS
const lol = {
    lol1: "M",
    lol2: "G"
};
console.log(lol.lol1, lol.lol2);

const lmao = [1,2,3,4,5];
console.log(lmao[3]);

// LOOPS
for(let x=1;x<=10;x++){
    console.log(`New ${x}`);
}

while(x >= 20){
    console.log(x);
    x--;
}

do {
    x--;
    console.log(x);
}while(x >= 10);

let arr = [1,10,5,15,2,7,28,900,45,18,27];
console.log(arr.sort());