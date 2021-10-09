import Sequelize from "sequelize";
import jwt from "jsonwebtoken";
import bcrypt from "bcrypt";
import { pbkdf2Sync, randomBytes } from "crypto";
// https://thinkster.io/tutorials/node-json-api/creating-the-user-model
let { STRING, DATEONLY } = Sequelize;
const saltRounds = 10;

const UserSchema = {
  username: {
    unique: true,
    type: STRING,
    lowercase: true,
    required: [true, "can't be blank"],
    match: [/^[a-zA-Z0-9]+$/, "is invalid"],
    index: true,
    get() {
      const rawValue = this.getDataValue(username);
      return rawValue ? rawValue.toUpperCase() : null;
    },
  },
  email: {
    unique: true,
    type: STRING,
    lowercase: true,
    required: [true, "can't be blank"],
    match: [/\S+@\S+\.\S+/, "is invalid"],
    index: true,
  },
  firstName: STRING,
  middleName: STRING,
  lastName: STRING,
  dateOfBirth: DATEONLY,
  bio: STRING,
  image: STRING,
  hash: STRING,
};

export default UserSchema;
