---
layout: post
title: Calcular minutos em python
tags: python
---


```
from datetime import timedelta, datetime
print datetime.strptime('17:08', '%H:%M') - timedelta(minutes=72)
```


