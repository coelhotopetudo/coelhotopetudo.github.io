---
layout: post
title: 'Corrigindo sistema de arquivos no Ubuntu linux'
---

O computador da minha mãe, não estava iniciando, acusava algo como:


Para corrigir foi muito fácil, mas precisei do meu live USB com o ubuntu 16.04. Quando tentei acessar (pelo nautilus, porque direto da barra, não acontecia) o drive que estava o Ubuntu da minha mãe, avisou que precisava fazer verificação. usei o comando:

sudo fsck -f <caminho>

e dei um monte de <Enter> para corrigir cada erro, parece que se usar o argumento "-y" evita ter que dar <Enter> a cada erro, mas não testei, pois o comando sem o argumento e segurar o Enter, arrumou tudo.

Fonte: https://bbs.archlinux.org/viewtopic.php?id=179266
