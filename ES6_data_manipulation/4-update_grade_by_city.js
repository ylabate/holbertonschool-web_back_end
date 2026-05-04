export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  return studentsList.filter((student) => student.location === city).map((student) => {
    const newGrade = newGrades.find((newGrade) => newGrade.studentId === student.id)
    if (!newGrade) { student.grade = 'N/A'; }
    else { student.grade = newGrade.grade; }
    return student;
  });
}
