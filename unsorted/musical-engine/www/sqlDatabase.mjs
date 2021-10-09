import __dirname from "./config/core.mjs";
import { resolve } from "path";
import addressSchema from "./models/addresses.mjs";
import Sequelize from "sequelize";
import userSchema, { isAuthenticated } from "./models/users.mjs";
import postSchema from "./models/posts.mjs";
import webtokensSchema from "./models/webtokens.mjs";
import profileSchema from "./models/profiles.mjs";
const database = new Sequelize({
  dialect: "sqlite",
  storage: resolve(`${__dirname}/../../test.sqlite`),
  timestamps: true,
  deletedAt: "destroyTime",
  // paranoid: true
});
const Token = database.define("web_tokens", webtokensSchema);
const Post = database.define("posts", postSchema);
const User = database.define("user", userSchema);
const Profile = database.define("profile", profileSchema);
const Address = database.define("addresses", addressSchema);
// User.Addresses = User.hasMany(Address);
User.belongsTo(Profile);

export { Token, Post, User, Profile, database, isAuthenticated };
