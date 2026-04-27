export default function appendToEachArrayValue(array, appendString) {
  const res = [];
  for (const value of array.entries()) {
    res.push(appendString + value);
  }

  return res;
}
