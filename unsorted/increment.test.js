import increment from "../src/increment.js";
test.each([
  [2, 3],
  [-9, -8],
  [0, 1],
  [999, 1000],
  [73, 74],
])("increment value", (num, output) => {
  expect(increment(num)).toEqual(output);
});
