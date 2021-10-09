import bcrypt from "bcrypt";
export default async function passwordIsValid(data = {}) {
  let { password, hashedPassword } = data;
  return await new Promise((resolve, reject) =>
    bcrypt.compare(password, hashedPassword, (err, result) => {
      if (err) reject({ 400: "Invalid username and password" });
      resolve(result);
    }),
  );
}
