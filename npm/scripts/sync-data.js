'use strict';
// Copy the repo-level data and licence files into the package before packing.
const fs = require('fs');
const path = require('path');
const pkg = path.join(__dirname, '..');
const repo = path.join(pkg, '..');
fs.mkdirSync(path.join(pkg, 'data'), { recursive: true });
fs.copyFileSync(path.join(repo, 'index.json'), path.join(pkg, 'data', 'index.json'));
for (const f of ['LICENSE', 'LICENSE-CODE', 'NOTICE']) {
  fs.copyFileSync(path.join(repo, f), path.join(pkg, f));
}
console.log('synced data/index.json and licence files');
