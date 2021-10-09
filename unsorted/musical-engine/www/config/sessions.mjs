const middleware = (req, res, next) => {
  var err = req.session.error;
  var msg = req.session.success;
  delete req.session.error;
  delete req.session.success;
  res.locals.message = "";
  if (err) res.locals.message = '<p class="msg error">' + err + "</p>";
  if (msg) res.locals.message = '<p class="msg success">' + msg + "</p>";
  next();
};

const sessionConfig = {
  init: {
    resave: false, // don't save session if unmodified
    saveUninitialized: false, // don't create session until something stored
    secret: "shhhh, very secret",
  },
  middleware,
};
export default sessionConfig;
