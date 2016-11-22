---
layout: post
title: 'Palestra sobre GitLab'
---


# Nomes
* Git para projetos de código aberto
* Git: uma abordagem pŕatica para desenvolvedores
* GitLab/GitHub: uma introdução prática para desenvolvedores

# Resumo 
Uma introdução sobre como utilizar serviços como GitLab e GitHub para contribuir com softwares de código aberto.

# objetivo dessa palestra 
* será somente na web e podemos falar que existem outras formas de interação

# minha experiencia
* idéia de falar um pouco sobre minha experiencia com git/gitlab/github

# um pouco sobre git 
* Sistemas de Controle de Versão Distribuídos
* história, Linux e BitKeeper
* mais info ver site scm-git [1]
* O que é controle de versão, e por que você deve se importar? O controle de versão é um sistema que registra as mudanças feitas em um arquivo ou um conjunto de arquivos ao longo do tempo de forma que você possa recuperar versões específicas. [1]
* o commit do git é sempre primeiro no local (ou a sua cópia) e depois envia para o remoto (ou o repositório original via pull-request)
* Clonar um repositório é quando todo o controle de versão (todos os commits) é trazido para máquina local (git clone)

# GitLab e GitHub
* GitHub é um serviço, tem outros serviços além de um repositório git, por exemplo GH-Pages, Gist, Gitter
* github é uma rede social: https://github.com/about
* GitLab é uma solução e também um serviço, mais corporativo
** tem apropriação de horas
** integração contínua
* https://about.gitlab.com/comparison/gitlab-vs-github.html (parcial)
* outros (BitBucket, SourceForge, etc)

# criando meu primeiro projeto e primeiro commit 
* conta, criar uma, permite login social

# contribuindo com um projeto existente 
* será que alguém já não criou isso?
* fork 
* pull-request

# fork
* cópia total do projeto, inclusive commits
* rastreabilidade com o projeto original
* como identificar um fork
* gráfico de forks e merges [$1]
* exemplo de uma calculadora ( https://gitlab.com/coelhotopetudo/calculadora ), uma aplicação simples com somente função adicionar e que iremos implementar a função subtrair

# pull-request 
* uma proposta para o repositório original

# funcionalidades do gitlab
* visibilidade dos repositórios 
* criação de grupos 
* wiki
* issues

# Referências
    1 - https://git-scm.com/book/pt-br/v1

# Fazer
$1 - procurar gráfico fork
$2 - criar organizacao que possui uma calculadora já quase completa
$3 - ver como eh o glpages
