import bkfd2Password from "pbkdf2-password";
const hasher = bkfd2Password();
console.log(hasher);
