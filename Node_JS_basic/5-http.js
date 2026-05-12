const http = require('http');
const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => data.trim().split('\n').filter((line) => line.trim().length > 0))
    .then((lines) => lines.map((line) => line.split(',')).slice(1))
    .then((csv) => {
      let res = `Number of students: ${csv.length}`;

      const fields = {};
      for (const student of csv) {
        const fieldName = student[3];
        if (!fields[fieldName]) {
          fields[fieldName] = { number: 0, students: [] };
        }
        fields[fieldName].number += 1;
        fields[fieldName].students.push(student[0]);
      }
      for (const [field, value] of Object.entries(fields)) {
        res += `\nNumber of students in ${field}: ${value.number}. List: ${value.students.join(', ')}`;
      }
      return res;
    })
    .catch((err) => {
      throw Error('Cannot load the database');
    });
}

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(process.argv[2])
      .then((studentList) => {
        res.write(studentList);
        res.end();
      })
      .catch((err) => {
        res.write(err.message);
        res.end();
      })
  }
});

app.listen(1245);

module.exports = app;
