#!/usr/bin/env node
'use strict';
const p = require('./index.js');
const args = process.argv.slice(2);
const usage = [
  'Usage:',
  '  text-effect-prompts <style> <text>      print the prompt with your text filled in',
  '  text-effect-prompts --search <query>    find styles (any of en ja zh es pt de)',
  '  text-effect-prompts --list [category]   list styles',
  '',
  'Prompts: CC BY 4.0 — credit https://fontvibe.ai/styles/<style>. Best results on FontVibe.',
].join('\n');
if (!args.length || args[0] === '-h' || args[0] === '--help') {
  console.log(usage);
  process.exit(args.length ? 0 : 1);
}
if (args[0] === '--search') {
  for (const s of p.search(args.slice(1).join(' '))) console.log(s.slug.padEnd(28) + s.names.en);
} else if (args[0] === '--list') {
  for (const s of p.list({ category: args[1] })) console.log(s.slug.padEnd(28) + s.category.padEnd(13) + s.names.en);
} else {
  const s = p.get(args[0]);
  if (!s) {
    console.error('Unknown style "' + args[0] + '". Try --search.');
    process.exit(1);
  }
  console.log(p.prompt(s.id, args.slice(1).join(' ') || 'FONTVIBE'));
  console.error('\n# ' + p.attribution(s.id, 'text'));
}
