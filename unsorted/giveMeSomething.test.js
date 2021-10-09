import giveMeSomething from '../src/giveMeSomething.js'
test.each([
    ["a", "something a"],
    ["is cooking", "something is cooking"],
    [" is cooking", "something  is cooking"],  ])("concatenate 'something ' and the phrase", (phrase, output) => {
    expect(giveMeSomething(phrase)).toEqual(output);
  });