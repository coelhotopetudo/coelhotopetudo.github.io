---
layout: post
title: 'Fazendo o unity voltar a funcinoar para conta da minha mae'
---



Can someone affected by this please run

  gsettings get org.compiz.core:/org/compiz/profiles/unity/plugins/core/ active-plugins

  in a terminal and paste the output to this bug?

  Also please attach your ~/.xsession-errors file.

  Then try running

    gsettings reset org.compiz.core:/org/compiz/profiles/unity/plugins/core/ active-plugins

    and restarting/logging out and in to see if you get your session back.


fonte: https://bugs.launchpad.net/ubuntu/+source/compiz/+bug/1166765/comments/9
