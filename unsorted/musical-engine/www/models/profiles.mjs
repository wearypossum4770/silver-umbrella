import { Sequelize } from "sequelize";
import __dirname from "../config/core.mjs";
import { resolve } from "path";
const { STRING, BOOLEAN, DATE, VIRTUAL } = Sequelize.DataTypes;
const profileSchema = {
  preferDarkMode: {
    type: Boolean,
    defaultValue: false,
  },
  image: {
    type: STRING,
    defaultValue: resolve(`${__dirname}/../../src/assets/default.webp`),
  },
};

export default profileSchema;
