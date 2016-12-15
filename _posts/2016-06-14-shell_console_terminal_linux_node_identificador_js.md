---
layout: post
title: 'executando comando node no terminal linux'
---

```javascript
#!/usr/bin/env node
var exec = require('child_process').exec;
var child;
var comando = 'mocha --reporter spec --compilers coffee:coffee-script/register';

child = exec(
  'cd /home/coelho/git/gitlab.com/coisarada/identificador && ' 
  + comando, function (error, stdout, stderr) 
  {
    console.log(stdout);
  }
);

//press Enter to exit
process.stdin.resume();
process.stdin.setEncoding('utf8');
process.stdin.on('data', function (text) 
{
  process.exit();
});
```
