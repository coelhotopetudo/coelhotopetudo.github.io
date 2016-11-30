---
layout: post
title: 'Palestra sobre GitLab'
separator: "^\n\n\n"
---
# Abrindo seu código para o mundo! 
## GitLab/GitHub: uma introdução prática
* Alisson Coelho de Morais (coelhotopetudo@gmail.com) 
* Flávio Casas de Arcega
## pq (Flávio) 
> Em essência, falar de ferramentas de versionamento é falar de colaboração, é falar de trabalho em equipe, é falar de muitas pessoas trabalhando em cima de uma mesma base de código para juntos fazerem aquilo que sozinhas talvez não conseguiriam. 
## um pouco sobre git 
* Sistemas de Controle de Versão Distribuídos
* história: Linux e BitKeeper
* mais info ver site scm-git [1]
* O que é controle de versão
Note: e por que você deve se importar? O controle de versão é um sistema que registra as mudanças feitas em um arquivo ou um conjunto de arquivos ao longo do tempo de forma que você possa recuperar versões específicas. [1]
* o commit do git é sempre primeiro no local (ou a sua cópia) e depois envia para o remoto (ou o repositório original via pull-request)
* Clonar um repositório é quando todo o controle de versão (todos os commits) é trazido para máquina local (git clone)
## criando meu primeiro projeto e primeiro commit 
* criar uma conta, permite login social
* calculadora, primeiro somar
## contribuindo com um projeto existente 
* vamos impl as outras funcoes, mas será que alguém já não criou isso?
* fork 
* pull-request
## fork
* cópia total do projeto, inclusive commits
* rastreabilidade com o projeto original
* como identificar um fork
* https://gitlab.com/coelhotopetudo/calculadora
Notes:
* gráfico de forks e merges [$1]
* exemplo de uma calculadora, uma aplicação simples com somente função adicionar e que iremos implementar a função subtrair
## pull-request 
* proposta de codigo para o repositório original
* pode colocar um comentário explicando a mudanca
## os gits (Flávio)
> GitLab.com é a versão enterprise e gratuita para uso do software Gitlab, porém é possível baixar a versão Community para uso em servidor privado. GitHub é um serviço oferecido gratuitamente a projetos de código aberto semelhante ao gitlab.com porém não oferece uma versão para uso em servidores privados.

### Repositórios Públicos
* Github e Gitlab oferecem sem custo
### Repositórios Privados
* Github cobra
* Gitlab gratuito e ilimitado
## Referências
    1 - https://git-scm.com/book/pt-br/v1
    2 - https://github.com/about
    3 - https://about.gitlab.com/comparison/gitlab-vs-github.html
Note: eu achei essa comparação do gitlab um pouco, mas só um pouquinho parcial

## outros
### Resumo/Objetivo
* Mostrar, passo a passo, como é fácil compartilhar suas idéias com GitLab/GitHub, seja com seus próprios projetos ou em outros. Abordaremos como criar um repositório e também os conceitos fork e pull-request para colaborar com outros desenvolvedores.
### GitLab e GitHub
* GitHub é um serviço, tem outros serviços além de um repositório git, por exemplo GH-Pages, Gist, Gitter
* github é uma rede social: https://github.com/about
* GitLab é uma solução e também um serviço, mais corporativo
** tem apropriação de horas
** integração contínua
* https://about.gitlab.com/comparison/gitlab-vs-github.html (parcial)
* outros (BitBucket, SourceForge, etc)


### funcionalidades do gitlab
* visibilidade dos repositórios 
* criação de grupos 
* wiki
* issues
### Fazer:
$1 - procurar gráfico fork
$2 - criar organizacao que possui uma calculadora já quase completa
$3 - ver como eh o glpages
