import fs from "fs";
import mongoose from "moongoose";
import express from "express";
import session from "express-session";
import crypto from "crypto";
import passport from "passport";

import cors from "cors";
const PORT = 8000;

let fileName = "./src/components/core/backend.json";
const DB = JSON.parse(fs.readFileSync(fileName));
function checkDuplicate(prevState, state) {
  let previousState = new Set(prevState.map((obj) => obj.id));
  let target = state.filter((obj) => !previousState.has(obj.id));
  return [...prevState, ...target];
}
const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(passport.initialize());
app.use(passport.session());
app.use(cors());
try {
  app.get("/", (req, res) => {
    res.json(DB);
  });
  app.post("/", (req, res) => {
    let init = JSON.stringify(checkDuplicate(DB, req.body));
    console.log(init);
    res.send(init);
    fs.writeFileSync(fileName, init);
  });
} catch (err) {
  console.log(err);
}
app.listen(PORT, () => console.log(`Server started on port:${PORT}`));
