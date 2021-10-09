/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 *
 * */
export default function countMatches(items, ruleKey, ruleValue) {
  let count = 0;
  function counter(position) {
    items.forEach((item) => (item[position] === ruleValue ? count++ : count));
  }
  switch (ruleKey) {
    case "type":
      counter(0);
      break;
    case "color":
      counter(1);
      break;
    default:
      counter(2);
      break;
  }
  return count;
}
