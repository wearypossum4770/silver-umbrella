export default function isPalindrome(x) {
  if (x < 0) {
    return false;
  } else {
    let target = x.toString();
    let reversed = target.split("").reverse().join("");
    return target === reversed;
  }
}
