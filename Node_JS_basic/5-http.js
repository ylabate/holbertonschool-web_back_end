const http = require('http');
const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.trim().split('\n').filter((line) => line.length > 0);
    const csv = lines.map((line) => line.split(',')).slice(1);

    const fields = {};
    for (const student of csv) {
      const fieldName = student[3];
      if (!fields[fieldName]) {
        fields[fieldName] = { number: 0, students: [] };
      }
      fields[fieldName].number += 1;
      fields[fieldName].students.push(student[0]);
    }

    let res = `Number of students: ${csv.length}`;

    for (const [field, value] of Object.entries(fields)) {
      res += (`\nNumber of students in ${field}: ${value.number}. List: ${value.students.join(', ')}`);
    }
    return res;
  } catch (_) {
    throw Error('Cannot load the database');
  }
}

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    res.write(countStudents(process.argv[2]));
  }
  res.end();
});

app.listen(1245);

module.exports = app;
