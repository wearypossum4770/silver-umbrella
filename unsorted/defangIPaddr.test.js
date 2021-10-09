import defangIPaddr from "../src/defangIPaddr.js";
test.each([
  ["1.1.1.1", "1[.]1[.]1[.]1"],

  ["255.100.50.0", "255[.]100[.]50[.]0"],
])("defangs ip address", (test_input, expected) => {
  let func = defangIPaddr(test_input);
  expect(func).toBe(expected);
});
