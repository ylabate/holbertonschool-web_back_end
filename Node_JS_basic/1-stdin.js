const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log('Welcome to Holberton School, what is your name?');

const reponse = await rl.question();

rl.question('', (answer) => {
  console.log(`Your name is: ${answer}`);
  rl.close();
});

console.log('This important software is now closing');
