---
layout: post
title: 'Corrigindo sistema de arquivos no Ubuntu linux'
---

O computador da minha mãe, não estava iniciando, acusava algo como:

failed group descriptors corrputed

e que não poderia montar o / (root) e abria um console com o busybox.

Para iniciar pelo USB no computador da minha mãe, é um HPG42 velhinho tadinho, apertei: esc e depois f9

Para corrigir foi muito fácil, mas precisei do meu live USB com o ubuntu 16.04. Quando tentei acessar (pelo nautilus, porque direto da barra, não acontecia) o drive que estava o Ubuntu da minha mãe, avisou que precisava fazer verificação. usei o comando:

```
sudo fsck -f <caminho>
```

e dei um monte de ENTER para corrigir cada erro, parece que se usar o argumento "-y" evita ter que dar <Enter> a cada erro, mas não testei, pois o comando sem o argumento e segurar o Enter, arrumou tudo.

Fonte: https://bbs.archlinux.org/viewtopic.php?id=179266
