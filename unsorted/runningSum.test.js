import runningSum from "../src/runningSum.js";
test.each([
  [
    [1, 2, 3, 4],
    [1, 3, 6, 10],
  ],
  [
    [1, 1, 1, 1, 1],
    [1, 2, 3, 4, 5],
  ],
  [
    [3, 1, 2, 10, 1],
    [3, 4, 6, 16, 17],
  ],
])("determine running sum", (param1, output) => {
  let func = runningSum(param1);
  expect(func).toStrictEqual(output);
});
