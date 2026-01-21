// vulnerable.js

const http = require('http');
const fs = require('fs');
const url = require('url');

// 🚨 Hardcoded credentials
const DB_PASSWORD = 'admin123';

// 🚨 SQL Injection risk
function getUser(id) {
  const query = "SELECT * FROM users WHERE id = " + id;
  console.log("Running query:", query);
}

// 🚨 XSS vulnerability
function renderComment(comment) {
  return `<div>${comment}</div>`; // no sanitization
}

// 🚨 Insecure file read
function readFile(path) {
  return fs.readFileSync(path, 'utf8');
}

// 🚨 Unvalidated redirect
function redirectTo(targetUrl) {
  return `Redirecting to: ${targetUrl}`;
}

http.createServer((req, res) => {
  const query = url.parse(req.url, true).query;
  getUser(query.id);
  res.end(renderComment(query.comment));
}).listen(8080);
