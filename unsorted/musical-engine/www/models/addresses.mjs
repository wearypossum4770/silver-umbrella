import { Sequelize } from "sequelize";
const { STRING, BOOLEAN, DATE, VIRTUAL } = Sequelize.DataTypes;
const addressSchema = {
  type: STRING,
  line1: STRING,
  line2: STRING,
  city: STRING,
  state: STRING,
  zip: STRING,
};

export default addressSchema;
