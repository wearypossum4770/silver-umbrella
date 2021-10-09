const humanize = ({ fileSize }) => {
  let _size = Array.from(fileSize.toString());
  function inner() {
    switch (_size.length) {
      case 1:
        return fileSize === 1 ? `${fileSize} byte` : `${fileSize} bytes`;
      case 2:
      case 3:
        return `${fileSize} bytes`;
      case 4:
      case 5:
      case 6:
        return fileSize === 1000
          ? `${fileSize / 1000} kilobyte`
          : `${fileSize / 1000} kilobytes`;
      case 7:
      case 8:
      case 9:
        return fileSize === 1000000
          ? `${fileSize / 1000000} megabyte`
          : `${fileSize / 1000000} megabytes`;
      case 10:
      case 11:
      case 12:
        return fileSize === 1000000000
          ? `${fileSize / 1000000000} gigabyte`
          : `${fileSize / 1000000000} gigabytes`;

      // case 3:
      //         return "Tera Byte"
      // case 3:
      // return "Peta Byte"
      // case 3:
      // return "Exa Byte"
      // case 3:
      // return "Zetta Byte"
      // case 3:
      // return "Yotta Byte"
    }
  }
  return inner();
};
console.log(humanize({ fileSize: 0 }));
console.log(humanize({ fileSize: 1 }));
console.log(humanize({ fileSize: 4 }));
console.log(humanize({ fileSize: 14 }));
console.log(humanize({ fileSize: 714 }));
console.log(humanize({ fileSize: 1000 }));
console.log(humanize({ fileSize: 116010 }));
console.log(humanize({ fileSize: 1000000 }));
console.log(humanize({ fileSize: 26683198 }));
console.log(humanize({ fileSize: 1000000000 }));
console.log(humanize({ fileSize: 1535184120 }));
