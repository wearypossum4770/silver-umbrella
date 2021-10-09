import addition from "../src/addition.js";
test.each([
  [2, 3, 5],
  [-3, -6, -9],
  [7, 3, 10],
  [88, 2, 90],
])("increment value", (x, y, output) => {
  expect(addition(x, y)).toEqual(output);
});
