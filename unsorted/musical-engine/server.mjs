import { dirname } from "path";
import { fileURLToPath } from "url";
// import { createClient } from "redis";
// import pkg from "connect-redis";
// import cookieParser from "cookie-parser";
import express from "express";
import session from "express-session";
import {
  Token,
  Post,
  User,
  Profile,
  database,
  isAuthenticated,
} from "./www/sqlDatabase.mjs";
import sessionConfig from "./www/config/sessions.mjs";
import cors from "cors";
const __dirname = dirname(fileURLToPath(import.meta.url));
const PORT = 3002;
const json_url_config = { limit: "1mb", extended: true };
// https://www.liquidweb.com/kb/using-ssh-keys/
// subdomains mail , userpages, adminpages, portal
var app = express();
const getCookies = request =>
  Object.keys(request.signedCookies).length > 1
    ? request.signedCookies
    : request.cookies;
app.use(express.urlencoded(json_url_config));
app.use(express.json(json_url_config));
app.use(cors());
// app.use(cookieParser());
app.use(
  session({
    secret: "keyboard cat",
    saveUninitialized: true,
    resave: true,
    cookie: { maxAge: 60000 },
  }),
);
// app.use('/vue_socket_test')
app.use((req, res, next) => {
  var err = req?.session?.error;
  var msg = req?.session?.success;
  delete req?.session?.error;
  delete req?.session?.success;
  res.locals.message = "";
  if (err) res.locals.message = '<p class="msg error">' + err + "</p>";
  if (msg) res.locals.message = '<p class="msg success">' + msg + "</p>";
  next();
});
app.get("/api_images/:imageName", async (req, res)=> {
let {imageName} = req.params
res.sendFile(`/home/dragoomdoc/musical-engine/src/assets/profile_images/${imageName}`)

})
app.post("/uploads", async (req, res) => {
  // const readabale = createReadStream(fileName);
  // const writeable = createWriteStream(
  //   `${__dirname}/uploads/${username}/${fileName}`,
  // );
});
app.get("/api", async (req, res) => {
  let cookies = getCookies(req);
  console.log(req.headers.authorization);
  res.json({
    cookies: cookies,
    message: "HELLO WORLD",
  });
});
app.get("/", (req, res) => {
  console.log(req.session);
  res.send("<h1>Hello world</h1>");
});
app.post("/register", async (req, res) => {
  let instance = await User.build(req.body);
  let { dataValues, isNewRecord: created } = instance;
  // '$2b$10$2gK6W4aOgJHFYBEYtAH2aOQT8e/QnopXMxq19AJzn0dd6ELaGdd02',
  // salt: '$2b$10$2gK6W4aOgJHFYBEYtAH2aO',
  if (!created)
    return res
      .status(500)
      .json({ outgoingMessage: "There was a problem registering the user." });
  res
    .status(200)
    .json({ created, outgoingMessage: `new User:${dataValues.username}` });
  instance.save();
});
app.post("/login", async (req, res) => {
  let cookies = getCookies(req);

  let { username, password } = req.body;
  let instance = await User.findOne({ where: { username: username } });
  if (!instance)
    return res.status(404).json({ outgoingMessage: "No user found." });
  let auth = await isAuthenticated(password, instance.password);
  return res.status(200).json({ isAuthenticated: auth });
});
app.get("/logout", function (req, res) {
  req.session.destroy(function () {
    res.redirect("/");
  });
});
database.sync({ force: false }).then(() => {
  app.listen(PORT, () => {
    console.log(
      `\nCORS-enabled web server.\nlistening to port localhost:${PORT}`,
    );
  });
});
