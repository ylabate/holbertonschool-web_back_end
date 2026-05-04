export default function cleanSet(set, startString) {
  if (typeof startString !== 'string') return '';
  if (!startString) return ''
  const res = [];
  for (const string of set) {
    if (typeof string === 'string' && string.startsWith(startString)) { res.push(string.substring(startString.length)); }
  }
  return res.join('-');
}
