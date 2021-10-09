import { diskStorage } from "multer";
const storage = () =>
  diskStorage({
    destination: function (req, file, cb) {
      cb(null, "uploads/");
    },
    // https://stackabuse.com/handling-file-uploads-in-node-js-with-expres-and-multer/
    // By default, multer removes file extensions so let's add them back
    filename: function (req, file, cb) {
      cb(
        null,
        `${file.fieldname}-${Date.now()}${path.extname(file.originalname)}`,
      );
    },
  });
