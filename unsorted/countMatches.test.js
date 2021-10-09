import countMatches from "../src/countMatches.js";

test.each([
  [
    [
      ["phone", "blue", "pixel"],
      ["computer", "silver", "phone"],
      ["phone", "gold", "iphone"],
    ],
    "type",
    "phone",
    2,
  ],

  [
    [
      ["phone", "blue", "pixel"],
      ["computer", "silver", "lenovo"],
      ["phone", "gold", "iphone"],
    ],
    "color",
    "silver",
    1,
  ],
])("counts items", (param1, param2, param3, output) => {
  let func = countMatches(param1, param2, param3);
  expect(func).toBe(output);
});
