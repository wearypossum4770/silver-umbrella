import convertMinutesToSeconds from '../src/convertMinutesToSeconds.js'


test.each([
    [6, 360],
    [4, 240],
    [8, 480],
    [60, 3600],
  ])("increment value by one", (minutes, output) => {
    expect(convertMinutesToSeconds(minutes)).toEqual(output);
  });



