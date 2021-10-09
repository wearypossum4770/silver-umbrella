import bcrypt from "bcrypt";
// import { Sequelize } from "sequelize";
// const { STRING, BOOLEAN } = DataTypes;
const saltRounds = 10;
const isAuthenticated = () => null;
const authenticate = (username = "", password = "") => null;
const validatePassword = async (plainTextPassword, user) =>
  bcrypt.compare(plainTextPassword, user.hashedPassword, (err, result) =>
    err ? err.message : result,
  );
const hashedPassword = () => null;
const setPassword = async plainTextPassword => null;
const password_changed = (password, user, passwordValidators) => null;
// export const userSchema = {
//   firstName: { type: STRING, defaultValue: "" },
//   middleName: { type: STRING, defaultValue: "" },
//   lastName: { trim: true, type: STRING, defaultValue: "" },
//   date_of_birth: { type: Date },
//   username: { type: STRING, unique: true },
//   email: { type: STRING, unique: true, validate: { is: /.+\@.+\..+/ } },
//   do_not_contact: { type: BOOLEAN, defaultValue: false },
//   is_active: { type: BOOLEAN, defaultValue: true },
//   last_login: { type: Date, defaultValue: new Date() },
//   owasp_safe_password: { type: BOOLEAN, defaultValue: false },
//   password: { admin: false, type: STRING },
//   prompt_password_change: { type: BOOLEAN, defaultValue: false },
//   retention_only: { type: BOOLEAN, defaultValue: false },
//   indexes: [{ unique: true, fields: ["email"] }],
// };

setPassword("something");
