// src/utils.js
const crypto = require('crypto');

const generateHash = (input) => {
  const hash = crypto.createHash('sha256');
  hash.update(input);
  return hash.digest('hex');
};

module.exports = { generateHash };
