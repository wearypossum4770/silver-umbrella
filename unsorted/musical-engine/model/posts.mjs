import Sequelize from "sequelize";
let { STRING, TEXT, ENUM } = Sequelize;
const PostSchema = {
  title: STRING,
  body: TEXT,
  visibility: ENUM("public", "private"),
};
export default PostSchema;
