import isPalindrome from "../src/isPalindrome.js";
test.each([
  [-121, false],
  [121, true],
  [10, false],
])("correctly tests palidromes", (num, output) => {
  expect(isPalindrome(num)).toEqual(output);
});
