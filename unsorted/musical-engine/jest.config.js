module.exports = {
  transformIgnorePatterns: ["/node_modules/"],
  preset: "@vue/cli-plugin-unit-jest",
  transform: {
    "^.+\\.vue$": "vue-jest",
  },
};
