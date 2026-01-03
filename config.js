// src/config.js
require('dotenv').config();

const secretKey = process.env.SECRET_KEY;

module.exports = { secretKey };
