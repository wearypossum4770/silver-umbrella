import jwt from "jsonwebtoken";
import bcrypt from "bcrypt";
import { readFileSync } from "fs";
import { dirname } from "path";
import { fileURLToPath } from "url";
let obj = new Map();
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const privateKey = readFileSync(`${__dirname}/pem/key.pem`);
const saltRounds = 10;
export const user = JSON.parse(
  readFileSync(`${__dirname}/../data/new_registrant.json`),
).pop();

let errors = ["HERE"];

export default async function createUser({ plaintextPassword }) {
  jwt.sign({ foo: "bar" }, privateKey, { algorithm: "RS256" }, (err, token) => {
    if (err) errors.push({ jwtError: err });
    obj.set("token", token);
    console.log(obj);
  });
  console.log(obj);

  bcrypt.genSalt(saltRounds, (err, salt) => {
    if (err) errors.push({ saltError: err });
    bcrypt.hash(plaintextPassword, salt, (err, hash) => {
      if (err) errors.push({ hashError: err });
      obj.set("salt", salt);
      obj.set("hashedPassword", hash);
    });
  });
  obj.set("errors", errors);
  return obj;
}
