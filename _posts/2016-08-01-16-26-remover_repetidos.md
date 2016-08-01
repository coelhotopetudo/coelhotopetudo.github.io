---
layout: post
---

```
todos = '''rep1@alunos.utfpr.edu.br
rep1@alunos.utfpr.edu.br
admin@admin.com
admin@admin.com
admin@admin.com
admin@admin.com'''
total = 0;
anterior = ''
for linha in todos.split('\n'):
  if (anterior != linha):
    total+=1
    print linha
  anterior = linha
print total
```
