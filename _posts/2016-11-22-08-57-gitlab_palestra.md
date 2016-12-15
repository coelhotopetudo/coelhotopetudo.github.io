---
layout: post
title: 'Palestra sobre GitLab/GitHub'
theme: css/theme/solarized.css
separator: "^\n\n\n"
excerpt: 'Conteúdo da palestra para mostrar como é fácil compartilhar suas idéias com GitLab/GitHub, seja com seus próprios projetos ou em outros. Abordaremos como criar um repositório e também os conceitos fork e pull-request para colaborar com outros desenvolvedores.'
---
# Abrindo seu código para o mundo! 

## GitLab/GitHub: uma introdução prática
* Alisson Coelho de Morais (coelhotopetudo@gmail.com) 
* Flávio Casas de Arcega

Note: Esse é o conteúdo da palestra que foi feita no dia 06/dez/2016 ás 11h, e pode ser acessada [aqui (a palestra começa em 1h57min)](http://assiste.serpro.gov.br/supsd/video.php?nome=212037). Os [slides da apresentação podem ser acessados aqui](http://coelhotopetudo.github.io/static/reveal.js).



## Objetivo
* Mostrar, passo a passo, como é fácil compartilhar suas idéias com GitLab/GitHub, seja com seus próprios projetos ou em outros. Abordaremos como criar um repositório e também os conceitos fork e pull-request para colaborar com outros desenvolvedores.



## Pq? (Flávio) 
> "Em essência, falar de ferramentas de versionamento é falar de colaboração, é falar de trabalho em equipe, é falar de muitas pessoas trabalhando em cima de uma mesma base de código para juntos fazerem aquilo que sozinhas talvez não conseguiriam."



## Um pouco sobre git 
* Sistemas de Controle de Versão Distribuídos
* história: Linux e BitKeeper
* https://git-scm.com/book/pt-br/v1
* O que é controle de versão?
Note: e por que você deve se importar? O controle de versão é um sistema que registra as mudanças feitas em um arquivo ou um conjunto de arquivos ao longo do tempo de forma que você possa recuperar versões específicas. [1]
* o commit do git é sempre primeiro no local (ou a sua cópia) e depois envia para o remoto (ou o repositório original via pull-request)
* Clonar um repositório é quando todo o controle de versão (todos os commits) é trazido para máquina local (git clone)



## Meu primeiro projeto e primeiro commit 
* criar uma conta, permite login social
* calculadora, primeiro somar



## Contribuindo com um projeto existente 
* E as outras funções? Vamos implementá-las? Mas será que alguém já não criou isso?
* fork 
* pull-request



## Fork

![fork](http://coelhotopetudo.github.io/static/img/fork-git-workflow-release-cycle-3release.png)

* cópia total do projeto, inclusive commits
* rastreabilidade com o projeto original
* como identificar um fork
* https://gitlab.com/coelhotopetudo/calculadora
Note:
 gráfico de forks e merges [$1]
* exemplo de uma calculadora, uma aplicação simples com somente função adicionar e que iremos implementar a função subtrair



## Pull-request 
* proposta de código para o repositório original
* pode colocar um comentário explicando a mudanca



## Os gits (Flávio)
> "GitLab.com é a versão enterprise e gratuita para uso do software Gitlab, porém é possível baixar a versão Community para uso em servidor privado. GitHub é um serviço oferecido gratuitamente a projetos de código aberto semelhante ao gitlab.com porém não oferece uma versão para uso em servidores privados."



## GitHub e GitLab
* outros (BitBucket, SourceForge, etc)
* Repositórios Públicos - Github e Gitlab oferecem sem custo
* Repositórios Privados - Github cobra, Gitlab gratuito e limitado
* https://github.com/about
* https://about.gitlab.com/comparison/gitlab-vs-github.html
Note: eu achei essa comparação do gitlab um pouco, mas só um pouquinho parcial



## GitLab e GitHub (cont.)
* GitHub é um serviço, tem outros serviços além de um repositório git, por exemplo GH-Pages, Gist, Gitter
* GitHub mais para uma rede social: https://github.com/about
* GitLab é uma solução e também um serviço, mais corporativo
** tem apropriação de horas
** integração contínua
** https://about.gitlab.com/comparison/gitlab-vs-github.html (parcial)



## Referências
* https://git-scm.com/book/pt-br/v1
* https://github.com/about
* https://about.gitlab.com/comparison/gitlab-vs-github.html
* https://gitlab.com/coelhotopetudo/calculadora



## Obrigado!
* http://coelhotopetudo.github.io/

