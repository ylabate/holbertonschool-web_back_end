const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf-8')
    .then((data) => data.trim().split('\n').filter((line) => line.trim().length > 0))
    .then((lines) => lines.map((line) => line.split(',')).slice(1))
    .then((csv) => {
      console.log(`Number of students: ${csv.length}`);

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
        console.log(`Number of students in ${field}: ${value.number}. List: ${value.students.join(', ')}`);
      }
    })
    .catch(() => {
      throw Error('Cannot load the database');
    });
}

module.exports = countStudents;
