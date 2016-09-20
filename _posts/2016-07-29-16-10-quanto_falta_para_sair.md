---
layout: post
title: Calcular minutos em python (horário)
tags: python
---

ver [codigo](/static/horario.py)


```
from datetime import timedelta, datetime
print datetime.strptime('17:08', '%H:%M') - timedelta(minutes=72)
```


