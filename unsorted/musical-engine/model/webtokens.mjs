import Sequelize from "sequelize";
let { STRING } = Sequelize;
const WebTokenSchema = {
  token: STRING,
  salt: STRING,
};
export default WebTokenSchema;
