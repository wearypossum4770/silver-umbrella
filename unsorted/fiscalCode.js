/**
 * @copyright https://edabit.com/challenge/Pa2rHJ6KeRBTF28Pg
 *
 * */
let months = new Map([
  [1, "A"],
  [2, "B"],
  [3, "C"],
  [4, "D"],
  [5, "E"],
  [6, "H"],
  [7, "L"],
  [8, "M"],
  [9, "P"],
  [10, "R"],
  [11, "S"],
  [12, "T"],
]);
export default function fiscalCode({ name, surname, gender, dob }) {
  const consonants = /[^aeiou]/gi;
  const vowels = /[aeiou]/gi;
  function partOne() {
    if (surname.length < 3) {
      return `${surname}X`;
    } else {
      let part = surname.match(consonants);
      if (part.length >= 3) {
        return part.join("");
      } else {
        return [...part, surname.match(vowels)[0]].join("");
      }
    }
  }
  function partTwo() {
    let cPart = name.match(consonants);
    let vPart = name.match(vowels)[0];
    if (name.length < 3) {
      return `${cPart[0]}${vPart[0]}X`;
    } else {
      if (cPart.length === 3) {
        return cPart.join("");
      } else if (cPart.length > 3) {
        return `${cPart[0]}${cPart[2]}${cPart[3]}`;
      } else {
        return [...cPart, vPart[0]].join("");
      }
    }
  }
  function partThree() {
    let [day, month, year] = dob.split("/");
    let ending = "";
    if (gender === "M") {
      ending += parseInt(day) < 10 ? `0${day}` : day;
    } else {
      ending += parseInt(day) + 40;
    }
    return year.slice(-2) + months.get(parseInt(month)) + ending;
  }
  return `${partOne().toUpperCase()}${partTwo().toUpperCase()}${partThree()}`;
}
