---
layout: post
title: 'executando comando node no terminal linux'
date: 2016/06/14 09:02:05 -0300
---

{% highlight ruby %}

#!/usr/bin/env node
var exec = require('child_process').exec;
var child;
var comando = 'mocha --reporter spec --compilers coffee:coffee-script/register';

child = exec(
  'cd /home/00737990929/git/gitlab.com/coisarada/identificador && ' 
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

{% endhighlight %}
