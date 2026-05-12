const { error } = require('console');
const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.trim().split(/\n/);
    const csv = lines.map((line) => line.split(',')).slice(1);

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
  } catch (_) {
    throw Error('Cannot load the database');
  }
}

module.exports = countStudents;
