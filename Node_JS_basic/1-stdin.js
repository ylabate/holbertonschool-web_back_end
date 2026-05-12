import readline from 'readline/promises';

async function main() {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const reponse = await rl.question('Welcome to Holberton School, what is your name?\n');

  rl.close();

  console.log(`Your name is: ${reponse}`);


  console.log('This important software is now closing');
}

main();
